# Lecture 4: School Database

This project demonstrates how to create and manage a SQLite database for a school.  
The script generates a `school.db` file, creates tables, inserts sample data, and provides SQL queries for analysis.

## Features

- Automatically creates `school.db` if it does not exist  
- Creates two tables:
  - **students** — stores student ID, full name, and birth year
  - **grades** — stores student grades with subject and value (1–100)
- Inserts sample student and grade data
- Provides SQL queries for:
  - Fetching all grades for a specific student
  - Calculating average grades per student
  - Listing students born after a specific year
  - Listing subjects and their average grades
  - Finding top 3 students by average grade
  - Showing students who scored below 80 in any subject
- Uses indexes for optimized query performance
- Handles data integrity and type validation

## Project Structure

lecture_4/
- `main.py`           — Python script to create the database, tables, insert data, and indexes
- `queries.sql`       — SQL queries for analysis
- `school.db`         — Generated SQLite database
- `pyproject.toml`    — Poetry project configuration
- `README.md`         — Project documentation

## How to Run

Make sure you are in the `lecture_4` folder with the virtual environment activated:

```bash
python main.py