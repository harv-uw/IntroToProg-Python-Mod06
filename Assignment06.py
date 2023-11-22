# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using classes
# Change Log: (Who, When, What)
#   Zach Harvey,11.22.2023,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = ('---Course Registration Program---\n Select from the following menu:\n 1. Register a Student for a '
             'Course\n 2. Show current data\n 3. Save data to a file\n 4. Exit the program\n'
             '---------------------------------')
FILE_NAME: str = 'Enrollments.json'
# Define the Data Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file_obj = None
menu_choice: str = ""
student_data: dict = {}
students: list = []


# Processing
class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files
    ChangeLog:
    Zach Harvey,11,22,2023,Create Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_list: list):
        """
        This function reads student data from a given file
        ChangeLog:
        Zach Harvey,11,22,2023,Create Function
        :return: None
        """
        try:
            file = open(file_name, "r")
            student_list = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("JSON file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("A non-specific error occurred", e)
        return student_list

    @staticmethod
    def write_data_to_file(file_name: str, student_list: list):
        """
        This function reads student data from a given file
        ChangeLog:
        Zach Harvey,11,22,2023,Create Function
        :return: None
        """
        try:
            file_obj = open(file_name, "w")
            json.dump(student_list, file_obj)
            file_obj.close()
            print(f'Your data was written to the file {FILE_NAME}')
        except TypeError as e:
            IO.output_error_messages("Please check that the data is in a valid JSON format.", e)
        except Exception as e:
            IO.output_error_messages("A non-specific error occurred", e)


# Presentation
class IO:
    """
    A collection of processing layer functions that manage user input and output
    ChangeLog:
    Zach Harvey,11,22,2023,Create Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays custom error messages to the user
        ChangeLog:
        Zach Harvey,11,22,2023,Create Function
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("--- Technical Error Message ---")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu choices to the user
        ChangeLog:
        Zach Harvey,11,22,2023,Create Function
        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        This function gets a menu choice from the user
        ChangeLog:
        Zach Harvey,11,22,2023,Create Function
        :return: string
        """
        choice = "0"
        try:
            choice = input("What would you like to do: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please choose a valid menu option")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def output_student_data(student_list: list):
        """
        This function displays current student data
        ChangeLog:
        Zach Harvey,11,22,2023,Create Function
        :return: None
        """
        if not student_list:
            print('There is no data currently stored.')
        else:
            for student in student_list:
                print(f'{student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')

    @staticmethod
    def input_student_data(student_list: list):
        """
        This function displays current student data
        ChangeLog:
        Zach Harvey,11,22,2023,Create Function
        :return: None
        """
        try:
            student_first_name = input("Please enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Please enter the student's last name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the course name: ")

            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            student_list.append(student_data)
        except ValueError as e:
            IO.output_error_messages("Incorrect data type.", e)
        except Exception as e:
            IO.output_error_messages("Non-specific error occurred", e)
        return student_list


students = FileProcessor.read_data_from_file(FILE_NAME, students)

# Present and Process the data
# Present the menu of choices
while True:
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        IO.input_student_data(students)
        continue
    # Present the current data
    elif menu_choice == "2":
        IO.output_student_data(students)
        continue
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
        continue
    # Stop the loop
    elif menu_choice == "4":
        print('Exiting...')
        break
    # Default case
    else:
        print("\nPlease enter a menu option.")
