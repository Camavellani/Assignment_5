import sqlite3
from user import user
database = sqlite3.connect("new data.db")
cursor = database.cursor()
class student(user):
    # Constructor
    def __init__(self, set_first, set_last, set_id):
        self.first_name = set_first
        self.last_name = set_last
        self.id = set_id

    # Method
    def add_courses(self, list):
        crn = input("Please type the CRN of the course you want to add.\n")
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?""", (crn,))
        query_result = cursor.fetchall()
        if(len(query_result) == 0):
            print("There was an error adding the course to your schedule. The CRN may not exist. Please try again.\n")
        else:
            print("Course successfully added.\n")
            list.append(query_result)
        return(list)
    def remove_courses(self, list):
        crn = input("Please type the CRN of the course you want to remove.\n")
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?""", (crn,))
        query_result = cursor.fetchall()
        if(len(query_result) == 0):
            print("There was an error removing the course from your schedule. The CRN may not exist. Please try again.\n")
        else:
            print("Course successfully removed.\n")
            list.remove(query_result)
    def print_schedule(self, list):
        return(list)
