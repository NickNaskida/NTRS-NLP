from src.extensions import celery


@celery.task()
def process_pdf_file(pdf_filename_secured):
    pass
