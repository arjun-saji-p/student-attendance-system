def menu():
    print("\n===== STUDENT ATTENDANCE SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3.Search Student") 
    print("4.Delete Student") 
    print("5. Mark Attendance")
    print("6. View Attendance")
    print("7. Exit")

def add_student():
    name = input("Enter student name: ")

    with open("students.txt", "a") as file:
        file.write(name + "\n")

    print("Student added successfully!")

def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        print("\nStudent List:")
        for student in students:
            print(student.strip())

    except FileNotFoundError:
        print("No students found.")
        
def search_student():
    name = input("Enter student name to search: ")

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        found = False

        for student in students:
            if student.strip().lower() == name.lower():
                found = True
                break

        if found:
            print("Student Found!")
        else:
            print("Student Not Found!")

    except FileNotFoundError:
        print("No student records found.")

def delete_student():
    name = input("Enter student name to delete: ")

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        found = False

        with open("students.txt", "w") as file:
            for student in students:
                if student.strip().lower() != name.lower():
                    file.write(student)
                else:
                    found = True

        if found:
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    except FileNotFoundError:
        print("No student records found.")
        
def mark_attendance():
    name = input("Enter student name: ")
    status = input("Present (P) / Absent (A): ")

    with open("attendance.txt", "a") as file:
        file.write(f"{name},{status}\n")

    print("Attendance marked successfully!")

def view_attendance():
    try:
        with open("attendance.txt", "r") as file:
            records = file.readlines()

        print("\nAttendance Records:")

        for record in records:
            print(record.strip())

    except FileNotFoundError:
        print("No attendance records found.")

while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student() 
    
    elif choice == "4":
        delete_student() 
        
    elif choice == "5":
        mark_attendance()

    elif choice == "6":
        view_attendance()

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
