"""
ORM models for the Book API.

Defines the SQLAlchemy ORM model for the Book entity.
"""

from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):
    """ORM model representing a book object in the database."""

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=True)
