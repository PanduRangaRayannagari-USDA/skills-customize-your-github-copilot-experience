# 📘 Assignment: CSV Gradebook Analyzer

## 🎯 Objective

Build a Python program that reads and validates grade records from a CSV file. You will use the standard library to turn raw records into useful class statistics and a readable report.

## 📝 Tasks

### 🛠️ Load and Validate Grade Records

#### Description
Complete `load_grades` in `starter-code.py` to read `grades.csv`. Each valid row should become a dictionary containing a student's name, assignment name, and numeric score.

#### Requirements
Completed program should:

- Use Python's `csv` module and a `with` statement to read `grades.csv`
- Accept only rows with a non-empty student name and assignment name, and a score from 0 through 100
- Skip invalid rows and print a message that includes the skipped row number

### 🛠️ Create a Grade Summary Report

#### Description
Complete the remaining functions to calculate each student's average score and write a text report named `grade_report.txt`.

#### Requirements
Completed program should:

- Calculate each student's average score rounded to one decimal place
- Include the class average and the highest-scoring student in `grade_report.txt`
- Print the same summary information to the terminal
