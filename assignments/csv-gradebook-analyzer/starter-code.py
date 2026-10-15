import csv


def load_grades(filename):
    """Return valid grade records from filename."""
    grades = []

    # Read the CSV file and add valid rows to grades.
    # Print a helpful message when you skip an invalid row.

    return grades


def calculate_student_averages(grades):
    """Return a dictionary mapping each student to their average score."""
    averages = {}

    # Calculate and store each student's average score.

    return averages


def create_report(averages):
    """Return the text for the grade summary report."""
    report = []

    # Add one line per student, then add the class average
    # and highest-scoring student.

    return "\n".join(report)


def main():
    grades = load_grades("grades.csv")
    averages = calculate_student_averages(grades)
    report = create_report(averages)

    print(report)

    with open("grade_report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report)


if __name__ == "__main__":
    main()
