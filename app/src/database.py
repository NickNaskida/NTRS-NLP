"""Database module, including the SQLAlchemy database object and DB-related utilities."""
from typing import Optional, Type, TypeVar

from flask_sqlalchemy import SQLAlchemy

from .compat import basestring

T = TypeVar("T", bound="PkModel")

# Alias common SQLAlchemy names
db = SQLAlchemy()
Column = db.Column
relationship = db.relationship


class CRUDMixin(object):
    """
    Mixin that adds convenience methods for CRUD (create, read, update, delete) operations.

    :methods:
        create: Create object
        :update: Update object
        :save: Save object
        :delete: Delete object
    """

    @classmethod
    def create(cls, **kwargs):
        """
        Create a new record and save it the database.

        :param kwargs: key arguments for attributes
        :return:
        """
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit: bool = True, **kwargs):
        """
        Update specific fields of a record.

        :param commit: default is True, specifies whether to save object to database
        :param kwargs: key arguments for attributes
        """
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        if commit:
            return self.save()
        return self

    def save(self, commit: bool = True):
        """
        Save the record.

        :param commit: default is True, specifies whether to save object to database
        """
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit: bool = True) -> None:
        """
        Remove the record from the database.

        :param commit: default is True, specifies whether to save object to database
        """
        db.session.delete(self)
        if commit:
            return db.session.commit()
        return


class Model(CRUDMixin, db.Model):  # type: ignore
    """Base model class that includes CRUD convenience methods."""

    __abstract__ = True

    @classmethod
    def load_all(cls) -> list:
        """
        Load all table data.

        :return: all table data
        """
        return cls.query.all()


class PkModel(Model):
    """Base model class that includes CRUD convenience methods, plus adds a 'primary key' column named ``id``."""

    __abstract__ = True

    id = Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls: Type[T], record_id) -> Optional[T]:
        """
        Get record by ID.

        :param record_id: ID of object
        :return: Pkmodel | None
        """
        if any(
                (
                        isinstance(record_id, basestring) and record_id.isdigit(),  # noqa: E126
                        isinstance(record_id, (int, float)),
                )
        ):
            return cls.query.get(int(record_id))
        return None


def reference_col(table_name, nullable=False, pk_name="id", foreign_key_kwargs=None, column_kwargs=None):
    """
    Column that adds primary key foreign key reference.

    :usage:
        category_id = reference_col('category')
        category = relationship('Category', backref='categories')
    """
    foreign_key_kwargs = foreign_key_kwargs or {}
    column_kwargs = column_kwargs or {}

    return Column(
        db.ForeignKey(f"{table_name}.{pk_name}", **foreign_key_kwargs),
        nullable=nullable,
        **column_kwargs,
    )
