class Assignment:
    def __init__(self, subject, title, score, max_score, due_date, assignment_type):
        self.subject = subject.lower().strip()              #to remove any leading/trailing whitespace 
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
            print("Filtering Assignments...")
        elif choice == '5':
            print("Showing Summary...")
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 0 to 5.")

if __name__ == "__main__":
    main()