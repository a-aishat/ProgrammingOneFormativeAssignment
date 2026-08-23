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


if __name__ == "__main__":
    main()