import os
from organization_data import Organization
from prettytable import PrettyTable

organization = Organization()


class Admin:
    def __init__(self):
        self.__CREDENTIALS = {
            "username": "admin234987",
            "password": "234987@cbs"
        }

        self.__WORKING_DAYS = {
            "jan": 23,
            "feb": 21,
            "mar": 22,
            "apr": 22,
            "may": 23,
            "jun": 20,
            "jul": 23,
            "aug": 22,
            "sep": 22,
            "oct": 23,
            "nov": 21,
            "dec": 23,
        }

        self.TOTAL_ANNUAL_WORKING_DAYS = 265

        self.__admin_options = """Below are the options you have access to:
1. Show all employees.
2. Show Attendance of all employees.
3. Check for defaulters
4. Show attendance of specific department"""

        self.__table = PrettyTable()

    def get_annual_working_days(self):
        """function will return the total working days of the year."""
        return self.TOTAL_ANNUAL_WORKING_DAYS

    def login_status(self, username, password):
        """function will check for admin successful."""
        if username == self.__CREDENTIALS['username'] and password == self.__CREDENTIALS['password']:
            os.system("cls")
            print("Login Successful. Welcome Admin to the system")
            self.show_options()
        else:
            print("You have entered wrong credentials. Sorry Login Failed")

    def show_full_attendance_list(self):
        """function will show the attendance of all the employees including managers."""
        data = organization.show_all_employees_full_attendance()
        self.__table.field_names = data[0]
        self.__table.add_rows(data[1])
        self.__table.sortby = "department"
        print(self.__table)
        self.__table = PrettyTable()

    def show_options(self):
        """function will ask user their task and will operate accordingly."""
        want_to_continue = True
        while want_to_continue:
            print(self.__admin_options)
            user_choice = int(input("Enter your task number or 0 to exit: "))
            os.system("cls")
            if user_choice == 0:
                want_to_continue = False
            else:
                self.admin_options(user_choice)
        print("Thanks Admin for using this system!.")

    def checking_defaulters(self):
        """function will display all defaulters in the organization."""
        data = organization.show_all_employees_full_attendance()[1]
        self.__table.field_names = ["employee ID", "name","department", "working days"]
        for individual in data:
            if individual[4] < self.TOTAL_ANNUAL_WORKING_DAYS:
                self.__table.add_row([individual[0], individual[1], individual[3], individual[-1]])
        print(self.__table)
        self.__table = PrettyTable()

    def department_attendance(self):
        """function will show the complete attendance based on the department requested """
        requested_department = input("Enter department [HR, Development, Testing, Design, Marketing, Support]: ")
        final_data = organization.show_all_employees_full_attendance()
        self.__table.field_names = final_data[0]
        for data in final_data[1]:
            if data[3] == requested_department:
                self.__table.add_row(data)
        self.__table.sortby = "designation"
        print(self.__table)
        self.__table = PrettyTable()

    def admin_options(self, choice):
        """function will operate based on the admin task choice."""
        if choice == 1:
            organization.show_all_employees()
        elif choice == 2:
            self.show_full_attendance_list()
        elif choice == 3:
            self.checking_defaulters()
        elif choice == 4:
            self.department_attendance()
        else:
            print("You have entered wrong option. Please enter correct option number.")
        # pass
