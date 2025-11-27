"""
Student Grade Analyzer
A console-based program for managing students and their grades.
Fulfills requirements of the laboratory assignment.
"""

# ----------------------------
#        DATA STORAGE
# ----------------------------

students = []
# List of dictionaries: {
#   "name": str,
#   "grades": list[int],
#   "avg": float | None  <-- cached average
# }


# ----------------------------
#       HELPER FUNCTIONS
# ----------------------------


def find_student(name: str):
    """Return a student dict by name, or None if not found."""
    for s in students:
        if s["name"].lower() == name.lower():
            return s
    return None


def calculate_average(student: dict):
    """
    Calculate and cache student's average grade.
    Returns a float or None (if no grades).
    """
    if not student["grades"]:
        student["avg"] = None
        return None

    try:
        avg = sum(student["grades"]) / len(student["grades"])
        student["avg"] = round(avg, 2)
        return student["avg"]
    except ZeroDivisionError:
        student["avg"] = None
        return None


def get_all_valid_averages():
    """
    Return a list of all valid (non-None) student averages.
    """
    return [s["avg"] for s in students if s["avg"] is not None]


# ----------------------------
#      MENU OPERATIONS
# ----------------------------


def add_student():
    """Add a new student to the system."""
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if find_student(name):
        print("This student already exists.")
        return

    students.append({"name": name, "grades": [], "avg": None})
    print(f"Student '{name}' added.")


def add_grade():
    """Add one or more grades to an existing student."""
    name = input("Enter student name: ").strip()
    student = find_student(name)

    if not student:
        print("Student not found.")
        return

    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip()

        if grade_input.lower() == "done":
            # Recalculate cached average
            calculate_average(student)
            break

        try:
            grade = int(grade_input)
            if not (0 <= grade <= 100):
                print("Grade must be between 0 and 100.")
                continue

            student["grades"].append(grade)
            print(f"Added grade {grade}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_report():
    """Print a full report for all students."""
    if not students:
        print("No students available.")
        return

    print("\n--- Student Report ---")

    for s in students:
        avg = calculate_average(s)

        if avg is None:
            print(f"{s['name']}'s average grade is N/A.")
        else:
            print(f"{s['name']}'s average grade is {avg}.")

    # Summary
    averages = get_all_valid_averages()
    if not averages:
        print("\nNo grades available to compute statistics.")
        return

    print("\n-----------")
    print(f"Max Average: {max(averages)}")
    print(f"Min Average: {min(averages)}")
    print(f"Overall Average: {round(sum(averages)/len(averages), 2)}")


def find_top_student():
    """Find and display the student with the highest average."""
    if not students:
        print("No students available.")
        return

    # Recalculate averages for all students
    for s in students:
        calculate_average(s)

    valid_students = [s for s in students if s["avg"] is not None]

    if not valid_students:
        print("No valid grades available.")
        return

    top = max(valid_students, key=lambda s: s["avg"])
    print(
        f"The student with the highest average is {top['name']} with a grade of {top['avg']}."
    )


# ----------------------------
#         MAIN LOOP
# ----------------------------


def main():
    """Main program menu loop."""
    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")

        try:
            choice = int(input("Enter your choice: ").strip())
        except ValueError:
            print("Invalid choice. Enter a number from 1 to 5.")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            add_grade()
        elif choice == 3:
            show_report()
        elif choice == 4:
            find_top_student()
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


# Run program
if __name__ == "__main__":
    main()
