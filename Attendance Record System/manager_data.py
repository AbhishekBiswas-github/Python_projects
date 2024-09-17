from prettytable import PrettyTable
from organization_data import Organization
from admin_data import Admin
import os

organization = Organization()
admin = Admin()


class Manager:
    def __init__(self):
        self.__manager_options = f"""1. Show all employees of the department.
2. Checking Defaulters
3. Show attendance"""

        self.__TOTAL_ANNUAL_WORKING_DAYS = admin.get_annual_working_days()

        self.__details = {}

        self.__table = PrettyTable()

    def set_my_details(self, owner_details):
        self.__details = owner_details

    def self_attendance(self):
        print(f"Hello {self.__details['name']}, You have worked "
              f"{organization.annual_attendance(self.__details['employee_ID'])} "
              f"out of {self.__TOTAL_ANNUAL_WORKING_DAYS} working days.")

    def department_attendance(self):
        final_data = organization.show_all_employees_full_attendance()
        self.__table.field_names = final_data[0]
        for data in final_data[1]:
            if data[3] == self.__details["department"]:
                self.__table.add_row(data)
        self.__table.sortby = "designation"
        print(self.__table)
        self.__table = PrettyTable()

    def checking_department_defaulters(self):
        data = organization.show_all_employees_full_attendance()[1]
        count = 0
        self.__table.field_names = ["employee ID", "name", "working days"]
        for individual in data:
            if individual[3] == self.__details["department"]:
                if individual[4] < self.__TOTAL_ANNUAL_WORKING_DAYS:
                    count += 1
                    self.__table.add_row([individual[0], individual[1], individual[-1]])
        if count == 0:
            print(f"There is no defaulters in {self.__details["department"]}")
        else:
            print(self.__table)
        self.__table = PrettyTable()

    def manager_options(self, choice):
        if choice == 1:
            self.department_attendance()
        elif choice == 2:
            self.checking_department_defaulters()
        elif choice == 3:
            self.self_attendance()
            pass

    def show_options(self):
        want_to_continue = True
        print(f"Welcome Manager {self.__details['name']} to the system.")
        while want_to_continue:
            print(self.__manager_options)
            user_choice = int(input("Enter your task or 0 for exit: "))
            os.system("cls")
            if user_choice == 0:
                want_to_continue = False
            else:
                self.manager_options(user_choice)
        print(f"Thanks Manager {self.__details['name']} for using the system.")
