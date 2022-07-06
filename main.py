import sqlite3
from unittest import result
from unittest.util import strclass
from user import user
from student import student
from instructor import instructor
from admin import admin

database = sqlite3.connect("data.db")
cursor = database.cursor()
course_list = []

# Creating tables
sql_command = """CREATE TABLE IF NOT EXISTS STUDENT (
    ID TEXT PRIMARY KEY NOT NULL,
    FIRST TEXT NOT NULL,
    LAST TEXT NOT NULL,
    YEAR INT NOT NULL,
    MAJOR TEXT NOT NULL,
    EMAIL TEXT NOT NULL);"""
cursor.execute(sql_command)
sql_command = """CREATE TABLE IF NOT EXISTS INSTRUCTOR (
    ID TEXT PRIMARY KEY NOT NULL,
    FIRST TEXT NOT NULL,
    LAST TEXT NOT NULL,
    TITLE TEXT NOT NULL,
    HIRE_YEAR INT NOT NULL,
    DEPARTMENT TEXT NOT NULL,
    EMAIL TEXT NOT NULL);"""
cursor.execute(sql_command)
sql_command = """CREATE TABLE IF NOT EXISTS ADMIN (
    ID TEXT PRIMARY KEY NOT NULL,
    FIRST TEXT NOT NULL,
    LAST TEXT NOT NULL,
    TITLE TEXT NOT NULL,
    OFFICE TEXT NOT NULL,
    EMAIL TEXT NOT NULL);"""
cursor.execute(sql_command)
sql_command = """CREATE TABLE IF NOT EXISTS COURSE (
    CRN TEXT PRIMARY KEY NOT NULL,
    TITLE TEXT NOT NULL,
    DEPARTMENT TEXT NOT NULL,
    TIME TEXT NOT NULL,
    DAYS TEXT NOT NULL,
    SEMESTER TEXT NOT NULL,
    YEAR INT NOT NULL,
    CREDITS INT NOT NULL);"""
cursor.execute(sql_command)
sql_command = """INSERT INTO STUDENT VALUES('000000', 'Andrew', 'Lee', 2023, 'BSCO', 'leea');"""
#cursor.execute(sql_command)
sql_command = """INSERT INTO COURSE VALUES('000000', 'Applied Programming Concepts', 'BSCO', '8:00AM-10:00AM', 'TR', 'Summer', 2022, 4);"""
#cursor.execute(sql_command)
sql_command = """INSERT INTO ADMIN VALUES('000000', 'George', 'Washington', 'President', 'Dobbs 140', 'washingtong');"""
#cursor.execute(sql_command)

user_choice = int(input(f'Choose a user type\n1. Student\n2. Instructor\n3. Admin\n'))

# UI - enter credentials
first = input("Enter your first name: \n")
last = input("Enter your last name: \n")
id = input("Enter your ID number without the W: \n")
if(user_choice == 1):
    # Verify student credentials
    cursor.execute("""SELECT ID FROM STUDENT WHERE ID = ?""", (id,))
    query_result1 = cursor.fetchall()
    cursor.execute("""SELECT FIRST FROM STUDENT WHERE FIRST = ?""", (first,))
    query_result2 = cursor.fetchall()
    cursor.execute("""SELECT LAST FROM STUDENT WHERE LAST = ?""", (last,))
    query_result3 = cursor.fetchall()
    if(len(query_result1) == 0):
        result_id = "0"
    else:
        result_id = id
    if(len(query_result2) == 0):
        result_first = "0"
    else:
        result_first = first
    if(len(query_result3) == 0):
        result_last = "0"
    else:
        result_last = last
elif(user_choice == 2):
    # Verify instructor credentials
    cursor.execute("""SELECT ID FROM INSTRUCTOR WHERE ID = ?""", (id,))
    query_result1 = cursor.fetchall()
    cursor.execute("""SELECT FIRST FROM INSTRUCTOR WHERE FIRST = ?""", (first,))
    query_result2 = cursor.fetchall()
    cursor.execute("""SELECT LAST FROM INSTRUCTOR WHERE LAST = ?""", (last,))
    query_result3 = cursor.fetchall()
    if(len(query_result1) == 0):
        result_id = "0"
    else:
        result_id = id
    if(len(query_result2) == 0):
        result_first = "0"
    else:
        result_first = first
    if(len(query_result3) == 0):
        result_last = "0"
    else:
        result_last = last
elif(user_choice == 3):
    # Verify admin credentials
    cursor.execute("""SELECT ID FROM ADMIN WHERE ID = ?""", (id,))
    query_result1 = cursor.fetchall()
    cursor.execute("""SELECT FIRST FROM ADMIN WHERE FIRST = ?""", (first,))
    query_result2 = cursor.fetchall()
    cursor.execute("""SELECT LAST FROM ADMIN WHERE LAST = ?""", (last,))
    query_result3 = cursor.fetchall()
    if(len(query_result1) == 0):
        result_id = "0"
    else:
        result_id = id
    if(len(query_result2) == 0):
        result_first = "0"
    else:
        result_first = first
    if(len(query_result3) == 0):
        result_last = "0"
    else:
        result_last = last
else:
    print("That was not a valid input. Please try again.\n")

# Successful Log In
if(id == result_id) and (first == result_first) and (last == result_last):
    while user_choice != 0:
    # Student
        if(user_choice == 1):
            student_user = student(first, last, id)
            print("Welcome, " + student_user.show_first() + " " + student_user.show_last() + "!")
            action_choice = int(input("Choose an option:\n1. Search courses\n2. Add courses\n3. Remove courses\n4. Print schedule\n5. Search course by parameter\n0. Exit\n"))
            if(action_choice == 1):
                print(student_user.search_courses())
            elif(action_choice == 2):
                print(student_user.add_courses(course_list))
            elif(action_choice == 3):
                print(student_user.remove_courses(course_list))
            elif(action_choice == 4):
                print(student_user.print_schedule(course_list))
            elif(action_choice == 5):
                print(student_user.search_by_parameters())
            elif(action_choice == 0):
                break
        
    # Instructor
        elif(user_choice == 2):
            instructor_user = instructor(first, last, id)
            print("Welcome, " + instructor_user.show_first() + " " + instructor_user.show_last() + "!")
            action_choice = int(input("Choose an option:\n1. Print schedule\n2. Print class list\n3. Search courses\n0. Exit\n"))
            if(action_choice == 1):
                print(instructor_user.print_schedule())
            elif(action_choice == 2):
                print(instructor_user.print_class_list())
            elif(action_choice == 3):
                print(instructor_user.search_courses())
            elif(action_choice == 0):
                break

    # Admin
        elif(user_choice == 3):
            admin_user = admin(first, last, id)
            print("Welcome, " + admin_user.show_first() + " " + admin_user.show_last() + "!")
            action_choice = int(input("Choose an option:\n1. Add course\n2. Remove course\n3. Add user\n4. Remove user\n5. Add student\n6. Remove student\n7. Add instructor\n8. Remove instructor\n0. Exit\n"))
            if(action_choice == 1):
                crn = "0"
                title = "0"
                depart = "0"
                time = "0"
                days = "0"
                semester = "0"
                year = 0
                credits = 0
                print(admin_user.add_course())
                cursor.execute("""INSERT INTO COURSE VALUES(?, ?, ?, ?, ?, ?, ?, ?);""", (crn, title, depart, time, days, semester, year, credits))
            elif(action_choice == 2):
                print(admin_user.remove_course())
            elif(action_choice == 3):
                print(admin_user.add_user())
            elif(action_choice == 4):
                print(admin_user.remove_user())
            elif(action_choice == 5):
                print(admin_user.add_student())
            elif(action_choice == 6):
                print(admin_user.remove_student())
            elif(action_choice == 7):
                print(admin_user.add_instuctor())
            elif(action_choice == 8):
                print(admin_user.remove_instructor())
            elif(action_choice == 0):
                break
else:
    print("There was an error signing in. Your name or W number might have been spelled incorrectly. Please try again.\n")

database.commit()
database.close()