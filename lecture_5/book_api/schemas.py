"""
Pydantic schemas for serialization and validation of book objects.
"""

from typing import Optional
from pydantic import BaseModel, Field


class BookBase(BaseModel):
    """Base schema containing shared fields for a book."""

    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: Optional[int] = Field(default=None, ge=0, le=2100)


class BookCreate(BookBase):
    """Schema for creating a new book."""

    pass


class BookUpdate(BaseModel):
    """Schema for updating book fields."""

    title: Optional[str] = Field(default=None, min_length=1)
    author: Optional[str] = Field(default=None, min_length=1)
    year: Optional[int] = Field(default=None, ge=0, le=2100)


class BookOut(BookBase):
    """Schema returned to the user."""

    id: int

    class Config:
        from_attributes = True
