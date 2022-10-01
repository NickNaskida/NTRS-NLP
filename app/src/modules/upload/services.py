import os
import uuid

import pdfplumber
from werkzeug.utils import secure_filename

from src.settings import Config
from src.jobs.tasks import process_pdf_file

# Temporary solution
from datetime import datetime
from src.jobs.services import extract_keywords_and_collocations
from src.modules.upload.models import FileModel


def process_uploaded_file(pdf_file, pdf_filename) -> None:
    pdf_filename = secure_filename(pdf_filename)
    pdf_filename_secured = generate_file_name(pdf_filename)
    pdf_file_path = os.path.join(Config.get_upload_path(), pdf_filename_secured)

    # Save file to uploads folder
    pdf_file.save(pdf_file_path)

    # Extract text from pdf file
    pdf_file_text = parse_pdf_text(pdf_file_path)

    # Call celery task
    # process_pdf_file.delay(pdf_file_text, pdf_filename, pdf_filename_secured)

    # Temporary solution
    keywords, collocations = extract_keywords_and_collocations(pdf_file_text)

    FileModel.create(
        pdf_filename=pdf_filename,
        pdf_filename_alt=pdf_filename_secured,
        keywords=keywords,
        collocations=collocations,
        upload_date=datetime.utcnow().date()
    )


def parse_pdf_text(file_path) -> str:
    """
    Extract text from pdf file.

    :param file_path: pdf file path
    :return: pdf extracted text
    """
    pdf_text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            pdf_text += extracted_text

    return pdf_text


def generate_file_name(file_name) -> str:
    """
    Generate a unique secure file name for the uploaded file.

    :param file_name: file name
    :return: secured filename
    """
    filename = str(uuid.uuid4()) + '--' + secure_filename(file_name)
    return filename

