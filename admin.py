# -*- coding: utf-8 -*-
# """admin

# Automatically generated by Colaboratory.

# Original file is located at
#     https://colab.research.google.com/drive/1F_gAZWwX9gzKodmLZOiVWwDonGLiVm0f
# """

import sqlite3
from user import user
database = sqlite3.connect("data.db")
cursor = database.cursor()
class admin(user):
    # Constructor
    def __init__(self, set_first, set_last, set_id):
        self.first_name = set_first
        self.last_name = set_last
        self.id = set_id

    def add_course(self):
      # ADDING FROM USER INPUT
      crn = str(input("Enter an id: "))
      title = str(input("Enter title: "))
      depart = str(input("Enter department: "))
      time = str(input("Enter what time of day the class is: "))
      days = str(input("Enter what days the class is: "))
      semester = str(input("Enter semester of class: "))
      year = int(input("Enter year of class: "))
      credits = int(input("Enter credits of class: "))
      cursor.execute("""INSERT INTO COURSE VALUES(?, ?, ?, ?, ?, ?, ?, ?);""", (crn, title, depart, time, days, semester, year, credits))

    def remove_course(self):
      crn = input("Enter a crn to delete:")
      sql_command = """DELETE FROM COURSE WHERE CRN = ?;""", (crn)
      cursor.execute(sql_command) 

    def add_user(self):  
      uid = input("Enter an id")
      fname = input("First name: ")
      lname = input("Last name: ")
      title = input("Enter title:")
      office = input("Enter an office:")
      email = input("Enter email:")
      cursor.execute("""INSERT INTO ADMIN VALUES(?, ?, ?, ?, ?, ?);""", (uid, fname, lname,title, office,email))

    def remove_user(self):
      id = input("Enter an id to delete:")
      id = int(id)
      sql_command = """DELETE FROM ADMIN WHERE ID = ?;""", (id)
      cursor.execute(sql_command) 
      
    def add_student(self):
      uid = input("Enter an id")
      fname = input("First name: ")
      lname = input("Last name: ")
      grad = input("Enter grad year:")
      major = input("Enter major:")
      email = input("Enter email:")
      cursor.execute("""INSERT INTO STUDENT VALUES(?, ?, ?, ?, ?, ?);""", (uid, fname, lname, grad,major,email))

    def remove_student(self):
      id = input("Enter an id to delete:")
      id = int(id)
      sql_command = """DELETE FROM STUDENT WHERE ID = ?;""", (id)
      cursor.execute(sql_command) 
    
    def add_instuctor(self):
      uid = input("Enter an id")
      fname = input("First name: ")
      lname = input("Last name: ")
      title = input("Enter title:")
      hire = input("Enter year of hire:")
      depart = input("Enter department:")
      email = input("Enter email:")
      cursor.execute("""INSERT INTO INSTRUCTOR VALUES(?, ?, ?, ?, ?, ?, ?);""", (uid, fname, lname,title, hire, depart,email))
    
    def remove_instructor(self):
      id = input("Enter an id to delete:")
      id = int(id)
      sql_command = """DELETE FROM INSTRUCTOR WHERE ID = ?;""", (id)
      cursor.execute(sql_command) 
    
    def search_course(self):
      cursor.execute("""SELECT * FROM COURSE""")
      query_result = cursor.fetchall()
      print(query_result)

database.commit()
database.close()