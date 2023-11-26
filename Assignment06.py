# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions with structured error handling
# Change Log: (Who, When, What)
#   Isabella McLaughlin, 11/22/2023, Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files
    ChangeLog: (Who, When, What)
    Isabella McLaughlin, 11/22/2023, Created Class
    """

    def read_data_from_file(file_name:str, student_data:list):
        """ This function reads the data from file
        ChangeLog: (Who, When, What)
        Isabella McLaughlin, 11/22/2023, Created Function
        :return: list
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem reading the file.", error=e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes the data to file
        ChangeLog: (Who, When, What)
        Isabella McLaughlin, 11/22/2023, Created Function
        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_and_course_name(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)
        finally:
            if file.closed == False:
                file.close()

# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output
    ChangeLog: (Who, When, What)
    Isabella McLaughlin, 11/22/2023, Created Class
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error message
        ChangeLog:
        Isabella McLaughlin, 11/22/2023, Created Function
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user
        ChangeLog: (Who, When, What)
        Isabella McLaughlin, 11/22/2023, Created Function
        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user
        ChangeLog: (Who, When, What)
        Isabella McLaughlin, 11/22/2023, Created Function
        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_name(student_data: list):
        """ This function displays the student and course name
        ChangeLog: (Who, When, What)
        Isabella McLaughlin, 11/22/2023, Created Function
        :return: None
        """
        # Process the data to create and display a custom message
        print()
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        print()

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student and course name
        ChangeLog: (Who, When, What)
        Isabella McLaughlin, 11/22/2023, Created Function
        :return: list
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="Error: One of the values was not the correct type of data.", error=e)

        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)

        return student_data



# START OF MAIN BODY

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!

        students=IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":

        IO.output_student_and_course_name(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
