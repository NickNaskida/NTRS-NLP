from src.database import PkModel, Column, db


class FileModel(PkModel):
    __tablename__ = 'files'

    pdf_filename = Column(db.String, nullable=False)
    pdf_filename_alt = Column(db.String, nullable=False)
    summarized_text = Column(db.Text, nullable=False)
    keywords = Column(db.Text, nullable=False)
    upload_date = Column(db.Date, nullable=False)
