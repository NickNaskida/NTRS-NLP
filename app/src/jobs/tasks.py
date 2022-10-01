from datetime import datetime

from src.extensions import celery
from src.modules.upload.models import FileModel
from src.jobs.services import extract_keywords_and_collocations


@celery.task()
def process_pdf_file(pdf_file_text, pdf_filename, pdf_filename_secured):
    from src.app import create_app

    with create_app().app_context():
        keywords, collocations = extract_keywords_and_collocations(pdf_file_text)

        FileModel.create(
            pdf_filename=pdf_filename,
            pdf_filename_alt=pdf_filename_secured,
            keywords=keywords,
            collocations=collocations,
            upload_date=datetime.utcnow().date()
        )
