"""
Lecture 5 - Simple Book Collection API

FastAPI application for managing a book collection using SQLAlchemy ORM.

Features:
- Add a book
- List all books with pagination
- Update a book
- Delete a book
- Search books by title, author, or year
"""

from fastapi import FastAPI, HTTPException, Depends, Path, Query
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel
from typing import Optional, List

# -----------------------------
# DATABASE SETUP
# -----------------------------

DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


class Book(Base):
    """SQLAlchemy ORM model for books."""

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=True)


Base.metadata.create_all(bind=engine)

# -----------------------------
# SCHEMAS
# -----------------------------


class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int] = None


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int]

    class Config:
        orm_mode = True


# -----------------------------
# DEPENDENCY
# -----------------------------


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# FASTAPI APP
# -----------------------------

app = FastAPI(title="Simple Book Collection API", version="1.0")

# -----------------------------
# ENDPOINTS
# -----------------------------


@app.post("/books/", response_model=BookResponse)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    """Add a new book."""
    db_book = Book(title=book.title, author=book.author, year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=List[BookResponse])
def list_books(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db),
):
    """Get all books with pagination."""
    return db.query(Book).offset(skip).limit(limit).all()


@app.get("/books/search/", response_model=List[BookResponse])
def search_books(
    title: Optional[str] = Query(None),
    author: Optional[str] = Query(None),
    year: Optional[int] = Query(None),
    db: Session = Depends(get_db),
):
    """Search books by title, author, or year."""
    query = db.query(Book)
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(Book.year == year)
    return query.all()


@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int = Path(..., ge=1),
    book: BookCreate = None,
    db: Session = Depends(get_db),
):
    """Update an existing book."""
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_book.title = book.title
    db_book.author = book.author
    db_book.year = book.year
    db.commit()
    db.refresh(db_book)
    return db_book


@app.delete("/books/{book_id}", response_model=BookResponse)
def delete_book(book_id: int = Path(..., ge=1), db: Session = Depends(get_db)):
    """Delete a book by ID."""
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return db_book


