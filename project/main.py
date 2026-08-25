class Assignment:
    def __init__(self, subject, title, score, max_score, due_date, assignment_type):
        self.subject = subject.strip()              #to remove any leading/trailing whitespace 
        #come back to this and find a way to adjust the case (take note of the user input and the filtering)
        self.title = title
        self.score = float(score)                           #to ensure that scores are stored/displayed as a float(decimal) for accurate calculations
        self.max_score = float(max_score)
        self.due_date = due_date
        self.type = assignment_type              #to store the type of assignment (e.g., homework, exam) for filtering and categorization

class Homework(Assignment):
    def __init__(self, subject, title, score, max_score, due_date):
        #calls the parent class constructor to initialize the common attributes and sets the assignment type to "homework"
        super().__init__(subject, title, score, max_score, due_date, "homework")

class Exam(Assignment):
    def __init__(self, subject, title, score, max_score, due_date):
        #calls the parent class constructor to initialize the common attributes and sets the assignment type to "exam"
        super().__init__(subject, title, score, max_score, due_date, "exam")

class GradeTracker:
    def __init__(self):
        self.assignments = []  #to store all assignments (homework and exams) in a list for easy management and retrieval during the program's execution

    def add_assignment(self, assignment):
        self.assignments.append(assignment)  #to add a new assignment to the list of assignments

    def list_assignments(self):
        if not self.assignments:             #to check if the assignments list is empty and display a message to the user if there are no assignments to list
            print("No assignments found.")   #this message is displayed when there are no assignments in the tracker to inform the user that they need to add assignments first
            return
        for assignment in self.assignments:  #to iterate through the list of assignments and print out the details of each assignment in a formatted manner for easy reading and understanding by the user
            print(f"{assignment.type.title()}: {assignment.title} | Subject: {assignment.subject} | Score: {assignment.score}/{assignment.max_score} | Due: {assignment.due_date}")

def add_homework(tracker):                   #to define a function that prompts the user for homework details, creates a Homework object, and adds it to the GradeTracker instance
    print("\n Add a new homework.")
    subject = input("Enter subject: ")
    title = input("Enter title: ")
    score = input("Enter score received: ")
    max_score = input("Enter maximum score possible: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    homework = Homework(subject, title, score, max_score, due_date)
    tracker.add_assignment(homework)         #it calls the add_assignment method of the GradeTracker instance to add the newly created Homework object to the list of assignments
    print(f"{subject} Homework added successfully.")   

def add_exam(tracker):                       #to define a function that prompts the user for exam details, creates an Exam object, and adds it to the GradeTracker instance
    print("\n Add a new exam.")
    subject = input("Enter subject: ")
    title = input("Enter title: ")
    score = input("Enter score received: ")
    max_score = input("Enter maximum score possible: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    exam = Exam(subject, title, score, max_score, due_date)
    tracker.add_assignment(exam)             #it calls the add_assignment method of the GradeTracker instance to add the newly created Exam object to the list of assignments
    print(f"{subject} Exam added successfully.")

def filter_assignments(tracker):                #to define a function that prompts the user for filtering criteria and displays the filtered assignments based on the user's input
    if not tracker.assignments:                     #to check if the assignments list is empty and display a message to the user if there are no assignments to filter
        print("No assignments found to filter.")
        return

    print("\n Filter Options:")
    print("1. Filter by Subject")
    print("2. Filter by Assignment Type (homework/exam)")
    print("3. Filter by Month")  

    choice = input("Select a filter option (1-3): ")
    filtered_assignments = []   #to initialize an empty list to store the assignments that match the filtering criteria specified by the user

    if choice == '1':
        subject_filter = input("Enter subject to filter by: ").strip().lower()  #to prompt the user for a subject to filter by and convert it to lowercase for case-insensitive comparison
        filtered_assignments = [a for a in tracker.assignments if a.subject.lower() == subject_filter]  #to create a list of assignments that match the specified subject
    elif choice == '2':
        type_filter = input("Enter assignment type to filter by (homework/exam): ").strip().lower()
        filtered_assignments = [a for a in tracker.assignments if a.type.lower() == type_filter]
    elif choice == '3':
        month_filter = input("Enter month to filter by (MM): ").strip().zfill(2)  #to prompt the user for a month to filter by and ensure it is in two-digit format (e.g., "01" for January)
        filtered_assignments = [a for a in tracker.assignments if len(a.due_date) >= 7 and a.due_date[5:7] == month_filter]  #to create a list of assignments that have a due date in the specified month, ensuring that the due date string is long enough to extract the month portion
    else:
        print("Invalid filter option selected.")
        return

#To display the filtered assignments to the user, the function checks if any assignments matched the filter criteria and prints them out in a formatted manner. If no assignments matched, it informs the user accordingly.
    if filtered_assignments:
        print("\nFiltered Assignments:")
        for assignment in filtered_assignments:
            print(f"{assignment.type.title()}: {assignment.title} | Subject: {assignment.subject} | Score: {assignment.score}/{assignment.max_score} | Due: {assignment.due_date}")  #this line formats and prints the details of each assignment in the filtered list, providing a clear overview of the assignments that match the user's filter criteria
    else:
        print("No assignments found matching the filter criteria.")

def show_summary(tracker):  #to define a function that calculates and displays a summary of the student's performance based on the assignments in the GradeTracker instance
    if not tracker.assignments:  #to check if the assignments list is empty and display a message to the user if there are no assignments to summarize
        print("No assignments found to summarize.")
        return

    total_count = len(tracker.assignments)  #to calculate the total number of assignments in the tracker
    total_score = sum(a.score for a in tracker.assignments)  #to calculate the total score received across all assignments
    total_max_score = sum(a.max_score for a in tracker.assignments)  #to calculate the total maximum score possible across all assignments
    average_score = (total_score / total_max_score) * 100 if total_max_score > 0 else 0  #to calculate the average score as a percentage, ensuring that division by zero is avoided if there are no assignments

    #to separate the assignments into homework and exams for calculated breakdown and detailed statistics
    homework_assignments = [a for a in tracker.assignments if a.type == "homework"]
    exam_assignments = [a for a in tracker.assignments if a.type == "exam"]

    print("\nSummary:")
    print(f"Total Assignments: {total_count}")
    print(f"Total Score: {total_score:.2f}/{total_max_score:.2f}")
    print(f"Average Score: {average_score:.2f}%")

    if homework_assignments:
        homework_score = sum(a.score for a in homework_assignments)
        homework_max_score = sum(a.max_score for a in homework_assignments)
        homework_average = (homework_score / homework_max_score) * 100 if homework_max_score > 0 else 0
        print(f"Homework Assignments: {len(homework_assignments)} | Total Score: {homework_score:.2f}/{homework_max_score:.2f} | Average Score: {homework_average:.2f}%")   
    #this block calculates and displays the total score, maximum score, and average score for homework assignments, providing a detailed breakdown of the student's performance in homework specifically.

    if exam_assignments:
        exam_score = sum(a.score for a in exam_assignments)
        exam_max_score = sum(a.max_score for a in exam_assignments)
        exam_average = (exam_score / exam_max_score) * 100 if exam_max_score > 0 else 0
        print(f"Exam Assignments: {len(exam_assignments)} | Total Score: {exam_score:.2f}/{exam_max_score:.2f} | Average Score: {exam_average:.2f}%")   
    #this block calculates and displays the total score, maximum score, and average score for exam assignments, providing a detailed breakdown of the student's performance in exams specifically.
    
    #average core per subject
    subject_map = {}  #to initialize an empty dictionary to store the total scores and maximum scores for each subject, allowing for the calculation of average scores by subject
    for assignment in tracker.assignments:
        subject = assignment.subject
        if subject not in subject_map:
            subject_map[subject] = {'total_score': 0, 'max_score': 0}  #to create a new entry in the subject_map dictionary for each unique subject, initializing the total score and maximum score to zero
        subject_map[subject]['total_score'] += assignment.score     #to accumulate the total score for each subject by adding the score of the current assignment to the existing total score in the subject_map dictionary
        subject_map[subject]['max_score'] += assignment.max_score

    print("\nAverage Scores by Subject:")
    for subject, scores in subject_map.items(): #to iterate through the subject_map dictionary and calculate the average score for each subject, displaying the results in a formatted manner for easy understanding by the user
        average = (scores['total_score'] / scores['max_score']) * 100 if scores['max_score'] > 0 else 0   #to calculate the average score for each subject as a percentage
        print(f"{subject}: {average:.2f}% ({scores['total_score']:.2f}/{scores['max_score']:.2f})")
        #this block calculates and displays the average score for each subject, providing a detailed breakdown of the student's performance across different subjects.

    # Highest and lowest scores
    highest_assignment = max(tracker.assignments, key=lambda a: (a.score / a.max_score) if a.max_score > 0 else 0) #to find the assignment with the highest score percentage, ensuring that division by zero is avoided if the maximum score is zero
    lowest_assignment = min(tracker.assignments, key=lambda a: (a.score / a.max_score) if a.max_score > 0 else 0)

    highest_percentage = (highest_assignment.score / highest_assignment.max_score) * 100 if highest_assignment.max_score > 0 else 0   
    lowest_percentage = (lowest_assignment.score / lowest_assignment.max_score) * 100 if lowest_assignment.max_score > 0 else 0   #to calculate the highest and lowest score percentages for the assignments with the highest and lowest scores, ensuring that division by zero is avoided if the maximum score is zero

    print("\nHighest Scoring Assignment:")
    print(f"{highest_assignment.type.title()}: {highest_assignment.title} | Subject: {highest_assignment.subject} | Score: {highest_assignment.score}/{highest_assignment.max_score} | Percentage: {highest_percentage:.2f}%")
    #this block displays the details of the assignment with the highest score percentage

    print("\nLowest Scoring Assignment:")
    print(f"{lowest_assignment.type.title()}: {lowest_assignment.title} | Subject: {lowest_assignment.subject} | Score: {lowest_assignment.score}/{lowest_assignment.max_score} | Percentage: {lowest_percentage:.2f}%")
    #this block displays the details of the assignment with the lowest score percentage

def main():
    tracker = GradeTracker()
    print("Welcome to the Student Grade/Assignment Tracker")

    while True:
        print("\n Main Menu:")
        print("1. Add Homework")
        print("2. Add Exam")
        print("3. List Assignments")
        print("4. Filter (by subject/assignment type/month)")
        print("5. Show Summary")
        print("0. Exit")

        choice = input("Select an option (0-5): ")

        if choice == '1':
            add_homework(tracker)     #it calls the add_homework function to prompt the user for homework details and add the new Homework object to the GradeTracker instance
        elif choice == '2':
            add_exam(tracker)    
        elif choice == '3':
            tracker.list_assignments()  #to call the list_assignments method of the GradeTracker instance to display all the assignments that have been added so far, providing the user with a clear overview of their current assignments and their details
        elif choice == '4':
            filter_assignments(tracker)
        elif choice == '5':
            show_summary(tracker)
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 0 to 5.")

if __name__ == "__main__":
    main()