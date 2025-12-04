"""
Lecture 4 — School Database

This script:
1) Creates school.db if it doesn't exist.
2) Creates required tables only if they are missing.
3) Inserts sample data ONLY once (only if tables were empty).
4) Executes all SQL queries required by the assignment.

Running it multiple times will NOT recreate the database
and will NOT insert duplicate records.
"""

import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).parent / "school.db"


# ------------------------------
# Utility
# ------------------------------
def print_section(title: str) -> None:
    print(f"\n--- {title} ---")


# ------------------------------
# Database Initialization
# ------------------------------
def initialize_database(conn: sqlite3.Connection) -> None:
    """Create tables if they do not exist and insert initial data if database is empty."""
    cursor = conn.cursor()

    # Create tables
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            birth_year INTEGER NOT NULL
        );
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            grade INTEGER NOT NULL CHECK(grade BETWEEN 1 AND 100),
            FOREIGN KEY(student_id) REFERENCES students(id)
        );
    """
    )

    # Check if data already inserted
    cursor.execute("SELECT COUNT(*) FROM students;")
    student_count = cursor.fetchone()[0]

    if student_count > 0:
        print("Database already initialized. Skipping data insertion.")
        return

    print("Database is empty. Inserting initial data...")

    # Insert students
    students = [
        ("Alice Johnson", 2005),
        ("Brian Smith", 2004),
        ("Carla Reyes", 2006),
        ("Daniel Kim", 2005),
        ("Eva Thompson", 2003),
        ("Felix Nguyen", 2007),
        ("Grace Patel", 2005),
        ("Henry Lopez", 2004),
        ("Isabella Martinez", 2006),
    ]
    cursor.executemany(
        "INSERT INTO students (full_name, birth_year) VALUES (?, ?);",
        students,
    )

    # Map IDs
    cursor.execute("SELECT id, full_name FROM students;")
    id_map = {name: sid for sid, name in cursor.fetchall()}

    # Insert grades
    grades = [
        (id_map["Alice Johnson"], "Math", 88),
        (id_map["Alice Johnson"], "English", 92),
        (id_map["Alice Johnson"], "Science", 85),
        (id_map["Brian Smith"], "Math", 75),
        (id_map["Brian Smith"], "History", 83),
        (id_map["Brian Smith"], "English", 79),
        (id_map["Carla Reyes"], "Science", 95),
        (id_map["Carla Reyes"], "Math", 91),
        (id_map["Carla Reyes"], "Art", 89),
        (id_map["Daniel Kim"], "Math", 84),
        (id_map["Daniel Kim"], "Science", 88),
        (id_map["Daniel Kim"], "Physical Education", 93),
        (id_map["Eva Thompson"], "English", 90),
        (id_map["Eva Thompson"], "History", 85),
        (id_map["Eva Thompson"], "Math", 88),
        (id_map["Felix Nguyen"], "Science", 72),
        (id_map["Felix Nguyen"], "Math", 78),
        (id_map["Felix Nguyen"], "English", 81),
        (id_map["Grace Patel"], "Art", 94),
        (id_map["Grace Patel"], "Science", 87),
        (id_map["Grace Patel"], "Math", 90),
        (id_map["Henry Lopez"], "History", 77),
        (id_map["Henry Lopez"], "Math", 83),
        (id_map["Henry Lopez"], "Science", 80),
        (id_map["Isabella Martinez"], "English", 96),
        (id_map["Isabella Martinez"], "Math", 89),
        (id_map["Isabella Martinez"], "Art", 92),
    ]
    cursor.executemany(
        "INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?);",
        grades,
    )

    conn.commit()
    print("Initial data inserted.")


# ------------------------------
# SQL Queries (Assignment)
# ------------------------------
def run_queries(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()

    # 1. Grades for Alice Johnson
    print_section("1. Grades for Alice Johnson")
    cursor.execute(
        """
        SELECT g.subject, g.grade
        FROM grades g
        JOIN students s ON s.id = g.student_id
        WHERE s.full_name = 'Alice Johnson';
    """
    )
    print(cursor.fetchall())

    # 2. Average grade per student
    print_section("2. Average grade per student")
    cursor.execute(
        """
        SELECT s.full_name, ROUND(AVG(g.grade), 2)
        FROM students s
        JOIN grades g ON g.student_id = s.id
        GROUP BY s.id
        ORDER BY AVG(g.grade) DESC;
    """
    )
    print(cursor.fetchall())

    # 3. Students born after 2004
    print_section("3. Students born after 2004")
    cursor.execute(
        """
        SELECT full_name, birth_year 
        FROM students
        WHERE birth_year > 2004;
    """
    )
    print(cursor.fetchall())

    # 4. Average grade per subject
    print_section("4. Average grade per subject")
    cursor.execute(
        """
        SELECT subject, ROUND(AVG(grade), 2)
        FROM grades
        GROUP BY subject
        ORDER BY AVG(grade) DESC;
    """
    )
    print(cursor.fetchall())

    # 5. Top 3 students
    print_section("5. Top 3 students with highest averages")
    cursor.execute(
        """
        SELECT s.full_name, ROUND(AVG(g.grade), 2)
        FROM students s
        JOIN grades g ON g.student_id = s.id
        GROUP BY s.id
        ORDER BY AVG(g.grade) DESC
        LIMIT 3;
    """
    )
    print(cursor.fetchall())

    # 6. Students with any grade <80
    print_section("6. Students with grades below 80")
    cursor.execute(
        """
        SELECT DISTINCT s.full_name
        FROM students s
        JOIN grades g ON g.student_id = s.id
        WHERE g.grade < 80
        ORDER BY s.full_name;
    """
    )
    print(cursor.fetchall())


# ------------------------------
# Main Entry
# ------------------------------
def main() -> None:
    conn = sqlite3.connect(DB_FILE)

    initialize_database(conn)
    run_queries(conn)

    conn.close()


if __name__ == "__main__":
    main()
