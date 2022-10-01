import uuid

import pdfplumber
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from transformers import pipeline
from werkzeug.utils import secure_filename

from src.settings import Config
from src.jobs.tasks import process_pdf_file


def process_uploaded_file(pdf_file, pdf_filename) -> None:
    pdf_filename_secured = generate_file_name(pdf_filename)

    # Save file to uploads folder
    pdf_file.save(Config.get_upload_path() + pdf_filename_secured)

    # Call celery task
    process_pdf_file.delay(pdf_filename_secured)


def generate_file_name(file_name) -> str:
    """
    Generate a unique secure file name for the uploaded file.

    :param file_name: file name
    :return: secured filename
    """
    filename = str(uuid.uuid4()) + '--' + secure_filename(file_name)
    return filename


def parse_pdf_text() -> str:
    pdf_text = ""

    with pdfplumber.open(r'19900018794.pdf') as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            pdf_text += extracted_text

    return pdf_text


def summarize_text(pdf_text):
    summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")

    summary = summarizer(pdf_text[:500], min_length=20, max_length=200)
    print(summary[0]['summary_text'])


def extract_keywords(pdf_text):
    stop_words = set(stopwords.words("english"))

    filtered_list = []
    for word in word_tokenize(pdf_text):
        if word.casefold() not in stop_words:
            if word.isalpha() and len(word) > 2:
                filtered_list.append(word)

    frequency_distribution = FreqDist(filtered_list)

    return frequency_distribution.most_common(30)
