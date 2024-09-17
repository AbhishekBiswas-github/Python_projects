from prettytable import PrettyTable
from organization_data import Organization
import os

organization = Organization()


class Employee:
    def __init__(self):
        self.__employee_record = {}

        self.__employee_options = """Below are the options you have access to:
1. Show attendance
2. Show all Month Attendance"""

        self.__table = PrettyTable()

    def set_employee_details(self, e_details):
        """function will fetch will details and save in the class attribute self.__employee_record"""
        self.__employee_record = e_details

    def show_attendance(self):
        """function will show the attendance"""
        print(f"Hello {self.__employee_record['name']}, you have worked"
              f" for {organization.annual_attendance(self.__employee_record['employee_ID'])} days.")

    def show_all_month_count(self):
        """function will show all the month's working days"""
        self.__table.field_names = ["Months", "working days"]
        for month in self.__employee_record['months']:
            self.__table.add_row([month.title(), self.__employee_record['months'][month]])
        print(self.__table)
        self.__table = PrettyTable()

    def show_options(self):
        """function will take user choice of the task they want to do"""
        want_to_continue = True
        print(f"Welcome {self.__employee_record['name']} to the system.")
        while want_to_continue:
            print(self.__employee_options)
            user_choice = int(input("Enter you task or 0 to exit: "))
            os.system("cls")
            if user_choice == 0:
                want_to_continue = False
            else:
                if user_choice == 1:
                    self.show_attendance()
                elif user_choice == 2:
                    self.show_all_month_count()
                else:
                    print("You have entered wrong option. Please enter correct option number.")
        print(f"Thanks for your visit {self.__employee_record['name']}.")
