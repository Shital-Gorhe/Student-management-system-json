
import sqlite3



connection = sqlite3.connect("students.db")
cursor = connection.cursor()

'''
CREATE DATABASE
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    marks INTEGER CHECK(marks >= 0 AND marks <= 100)
)
""")

connection.commit()

connection.close()

print("Database and table created successfully!")
'''




'''
ADD RECORD
def add_student(name, age, marks):
    cursor.execute("""
        INSERT INTO students (name, age, marks)
        VALUES (?, ?, ?)
    """, (name, age, marks))

    connection.commit()


add_student("Gauri", 25, 85)

connection.close()

print("Student added successfully!")
'''




'''
READ DATA
import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT * FROM students
""")

students = cursor.fetchall()

print(students)

connection.close()
'''




'''
SEARCH RECORD
def search_student(name):
    cursor.execute("""
        SELECT * FROM students
        WHERE name = ?
    """, (name,))

    student = cursor.fetchone()

    if student:
        print("ID:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Marks:", student[3])
    else:
        print("Student not found")


search_student("Gauri")

'''



''' 
MULTIPLE RECORD INSERTION and DISPLAY RECORD


def add_student(name, age, marks):
    cursor.execute(" " "
    INSERT INTO students (name, age, marks)
    VALUES (?, ?, ?)
    " " ",(name, age, marks))

    connection.commit()

add_student("shruti", 29, 99)
add_student("Akshay", 28, 44)
add_student("Sneha", 30, 77)

print("Student added successfully!")


cursor.execute("select * from students")

students = cursor.fetchall()

for student in students:
    print("ID:", student[0])
    print("Name:", student[1])
    print("Age:", student[2])
    print("Marks:", student[3])
    print()
    
connection.close()
'''

'''
TRY and EXCEPT EXCEPTION HANDLING

def add_student(name, age, marks):
    try:
        cursor.execute("""
            INSERT INTO students (name, age, marks)
            VALUES (?, ?, ?)
        """, (name, age, marks))

        connection.commit()
        print("Student added successfully!")

    except sqlite3.Error as error:
        print("Database error:", error)


add_student("Test", 20, 150)

connection.close()
'''

'''
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

print(students)
'''


def get_student_details():
    while True:
        name = input("Enter your name: ").strip()
        if name == "":
            print("Name can't be empty!")
            continue
        age = get_age()
        marks = get_marks()

        return name, age, marks
