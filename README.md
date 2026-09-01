# Student Grade & Assignment Tracker
This is a command-line interface application built in Python 3 to record, organize, filter and summarize student homework and exam scores within an active terminal session.

## Project Overview
The **Student Grade & Assignment Tracker** provides an efficient in-memory system to track students' academic performance. Using class inheritance, helper functions, and comprehensive input validation, it ensures reliable data entry and accurate grade calculations.

## Key Features
- **Object-Oriented Design**: Uses a base Assignment class with Homework and Exam classes that inherit from it using super().
- **Input Validation**: 
    - Ensures that scores are entered as numbers.
    - Prevents negative scores and scores higher than the maximum score possible.
    - Validates dates ensuring that they follow the YYYY-MM-DD format using datetime.
- **Assignment Filtering**: Allows assignments to be filtered by subject, assignment type (homework or exam), or the month they are due (MM). Subject searches are not case-sensitive.
- **Grade Summary**:
    - Calculates total grade and the overall percentage.
    - Shows separate results for homework and exams.
    - Calculates the average percentage for each subject.
    - Keeps track of the highest and lowest scoring assignments.
- **Data Management**: Stores assignment information in memory using lists of objects, so the data can be easily accessed while the program is running.

## Technical Specifications & Architecture
- **Language**: Python 3.14
- **Standard Library**: Uses `datetime` to handle and validate dates.
- **Class Structure**:
    - `Assignment`: The main class that stores information such as the `subject`, `title`, `score`, `maximum score`, `due date`, and `assignment type`.
    - `Homework(Assignment)`: Inherits the main attributes from `Assignment` and sets `type` as "homework".
    - `Exam(Assignment)`: Also inherits common attributes from `Assignment` and sets `type` as "exam".
    - `GradeTracker`: Keeps track of all the assignment objects and includes methods for adding and displaying assignments.

## Menu Structure
Main Menu:
1. Add Homework
2. Add Exam
3. List Assignments
4. Filter (by subject/assignment type/month)
5. Show Summary
0. Exit

## Sample Interactions
1. Adding and Validating an Assignment
```
Add a new homework.
Enter subject: Mathematics
Enter title: Algebra
Enter score received: 95
Enter maximum score possible: 100
Enter due date (YYYY-MM-DD): 2026-10-15
Mathematics Homework added successfully.

Add a new exam.
Enter subject: Biology
Enter title: Midterm Exam
Enter score received: 88
Enter maximum score possible: 100
Enter due date (YYYY-MM-DD): 2026-10-20
Biology Exam added successfully.
```

2. Listing Assignments
```
Homework: Algebra | Subject: Mathematics | Score: 95.0/100.0 | Due: 2026-10-15
Exam: Midterm Exam | Subject: Biology | Score: 88.0/100.0 | Due: 2026-10-20
```

3. Filtering Assignments by Month
```
Filter Options:
1. Filter by Subject
2. Filter by Assignment Type (homework/exam)
3. Filter by Month

Select a filter option (1-3): 3
Enter month to filter by (MM): 10

Filtered Assignments:
Homework: Algebra | Subject: Mathematics | Score: 95.0/100.0 | Due: 2026-10-15
Exam: Midterm Exam | Subject: Biology | Score: 88.0/100.0 | Due: 2026-10-20
```

4. Summary Output
```
Summary:
Total Assignments: 2
Total Score: 183.00/200.00
Average Score: 91.50%
Homework Assignments: 1 | Total Score: 95.00/100.00 | Average Score: 95.00%
Exam Assignments: 1 | Total Score: 88.00/100.00 | Average Score: 88.00%

Average Scores by Subject:
Mathematics: 95.00% (95.00/100.00)
Biology: 88.00% (88.00/100.00)

Highest Scoring Assignment:
Homework: Algebra | Subject: Mathematics | Score: 95.0/100.0 | Percentage: 95.00%

Lowest Scoring Assignment:
Exam: Midterm Exam | Subject: Biology | Score: 88.0/100.0 | Percentage: 88.00%
```
