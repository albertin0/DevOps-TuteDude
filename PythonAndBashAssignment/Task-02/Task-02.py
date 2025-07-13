
students = {}

while True:
    operation = input("\nEnter an Operation:\t1.Add a new Student and Grade\t2.Update an existing Student's Grade\t3.View all Students and Grades\t4.Exit\t\tEnter your choice(1, 2, 3, or 4): ")
    if operation == '4':
        print("Exiting the program.")
        break
    elif operation == '1':
        name = input("Enter the student's name: ")
        grade = input("Enter the student's grade: ")
        students[name] = grade
        print(f"Added {name} with grade {grade}.")
    elif operation == '2':
        name = input("Enter the student's name: ")
        if name in students:
            grade = input("Enter the new grade: ")
            students[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print(f"Student {name} not found.")
    elif operation == '3':
        if students:
            print("Students and Grades:")
            for student, grade in students.items(): # type: ignore
                print(f"{student}: {grade}")
        else:
            print("No students found.")
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")