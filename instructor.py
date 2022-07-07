import sqlite3
from user import user
# database file connection 
database = sqlite3.connect("data.db") 
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 
class instructor(user):
# Constructor
    def __init__(self, set_first, set_last, set_id):
        self.first_name = set_first
        self.last_name = set_last
        self.id = set_id
    # #Add courses to schedule
    # def add_courses(self, list):
    #     crn = input("Please type the CRN of the course you want to add.\n")
    #     cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?""", (crn,))
    #     query_result = cursor.fetchall()
    #     if(len(query_result) == 0):
    #         print("There was an error adding the course to your schedule. The CRN may not exist. Please try again.\n")
    #     else:
    #         print("Course successfully added.\n")
    #         list.append(query_result)
    #     return(list)
    # #Removing courses from schedule
    # def remove_courses(self, list):
    #     crn = input("Please type the CRN of the course you want to remove.\n")
    #     cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?""", (crn,))
    #     query_result = cursor.fetchall()
    #     if(len(query_result) == 0):
    #         print("There was an error removing the course from your schedule. The CRN may not exist. Please try again.\n")
    #     else:
    #         print("Course successfully removed.\n")
    #         list.remove(query_result) 
    #Print roster
    def print_roster(self, list):
        return(list)

    def assemble(self, list):
        ID = str(input("Enter a students W number (without the W) to add to your roster: "))
        cursor.execute("""SELECT * FROM STUDENT WHERE ID = ?""", (ID,))
        query_result = cursor.fetchall()
        if(len(query_result) == 0):
            print("There was an error adding the student to your roster. The W number may not exist. Please try again.\n")
        else:
            print("Student successfully added.\n")
            list.append(query_result)
        return(list)