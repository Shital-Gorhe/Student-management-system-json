import json

students = []

def load_students():
    with open("students.json", "r") as file:
        students = json.load(file)
        return students

try:
    students = load_students()

except FileNotFoundError:
    students = []


def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file)


def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))

            if age > 0:
                return age

            print("Age must be greater than 0.")

        except ValueError:
            print("Please enter a valid age.")


def get_marks():
    while True:
        try:
            marks = int(input("Enter your marks: "))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter valid marks.")


def get_student_details():
    while True:
        name = input("Enter your name: ").strip()
        if name == "":
            print("Name can't be empty!")
            continue
        age = get_age()
        marks = get_marks()

        return name, age, marks

def add_student():
    name, age, marks = get_student_details()

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    save_students()
    print("Student added successfully!")

def view_students():
    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])


def search_student():
    found = False
    name = input("Enter student name: ")
    for student in students:
        if student["name"] == name:
            found = True
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])

    if found:
        print("Student found successfully!")
    else:
        print("Student not found")


def update_student():
    found = False
    name = input("Enter student name for update: ")
    for student in students:
        if student["name"] == name:
            found = True
            student["age"] = int(input("Enter updated age: "))
            student["marks"] = int(input("Enter updated marks: "))
            print(student["name"])
            print(student["age"])
            print(student["marks"])
            save_students()

    if found:
        print("Student updated successfully!")
    else:
        print("Student not found")

def remove_student():
    found = False
    name = input("Enter student name to remove: ")
    for student in students:
        if student["name"] == name:
            found = True
            students.remove(student)
            save_students()

    if found:
        print("Student removed successfully!")
    else:
        print("Student not found")

def exit_program():
    print("Goodbye!")


while True:

    print("===== Student Management System =====")

    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Update student")
    print("5. Remove student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        remove_student()

    elif choice == 6:
        exit_program()
        break
    else:
        print("Invalid choice")


