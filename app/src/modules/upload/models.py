from src.database import PkModel, Column, db


class FileModel(PkModel):
    __tablename__ = 'files'

    filename = Column(db.String, nullable=False)
    summarized_text = Column(db.Text, nullable=False)
    keywords = Column(db.Text, nullable=False)
    upload_date = Column(db.Date, nullable=False)
