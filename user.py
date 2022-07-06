import sqlite3
database = sqlite3.connect("data.db")
cursor = database.cursor()
class user:
    # Constructor
    def __init__(self, set_first, set_last, set_id):
        self.first_name = set_first
        self.last_name = set_last
        self.id = set_id

    # Method
    def set_first(self, name):
        self.first_name = name
    def set_last(self, name):
        self.last_name = name
    def set_id(self, num):
        self.id = num
    def show_first(self):
        return self.first_name
    def show_last(self):
        return self.last_name
    def show_id(self):
        return self.id
    def search_courses(self):
        cursor.execute("""SELECT * FROM COURSE""")
        query_result = cursor.fetchall()
        print(query_result)
    def search_by_parameters(self):
        print("Enter a value or * to show all.")
        crn = input("Enter an id:")
        title = input("Enter title:")
        depart = input("Enter department:")
        time = input("Enter what time of day the class is:")
        days = input("Enter what days the class is:")
        semester = input("Enter semester of class:")
        year = int(input("Enter year of class:"))
        credits = input("Enter credits of class:")
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ? AND TITLE = ? AND DEPARTMENT = ? AND TIME = ? AND DAYS = ? and SEMESTER = ? AND YEAR = ? AND CREDITS = ?""" , [crn, title, depart, time, days, semester, year, credits])
