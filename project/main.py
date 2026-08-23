class Assignment:
    def __init__(self, subject, title, score, max_score, due_date, assignment_type):
        self.subject = subject.lower().strip()              #to remove any leading/trailing whitespace and convert to lowercase for consistency for easier search/filtering
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


def main():
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
            print("Adding Homework...")
        elif choice == '2':
            print("Adding Exam...")
        elif choice == '3':
            print("Listing Assignments...")
        elif choice == '4':
            print("Filtering Assignments...")
        elif choice == '5':
            print("Showing Summary...")
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 0 to 5.")

#To test the functionality of the main menu loop
if __name__ == "__main__":
    main()