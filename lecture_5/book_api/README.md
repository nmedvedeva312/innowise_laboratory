# Lecture 5: Simple Book Collection API

This project demonstrates creating a small web API to manage a personal book collection using **FastAPI** and **SQLAlchemy**.  
Users can add, view, update, delete, and search books stored in an SQLite database.

## Features

- Add a new book (`POST /books/`)
- Retrieve all books (`GET /books/`) with optional pagination (`skip` and `limit`)
- Update book details (`PUT /books/{book_id}`)
- Delete a book (`DELETE /books/{book_id}`)
- Search books by title, author, or year (`GET /books/search/`)
- SQLite database with SQLAlchemy ORM
- Input validation and serialization using Pydantic
- Handles errors and edge cases

## How to Run

Make sure you are in the `book_api` folder and have the virtual environment activated.

```bash
poetry run uvicorn main:app --reload