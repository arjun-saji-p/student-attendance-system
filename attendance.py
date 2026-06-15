attendance = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        attendance[name] = 0
        print("Student added successfully!")

    elif choice == "2":
        print(attendance)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
