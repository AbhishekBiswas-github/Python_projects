from prettytable import PrettyTable

table = PrettyTable()


class Organization:
    def __init__(self):
        self.__employees = [
            {
                "employee_ID": 101,
                "name": "Alice Johnson",
                "username": "alice.j",
                "password": "Al!ce2024",
                "designation": "Employee",
                "department": "Development",
                "salary": 85000,
                "months": {
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
            },
            {
                "employee_ID": 102,
                "name": "Bob Smith",
                "username": "bob.smith",
                "password": "Bob@123",
                "designation": "Manager",
                "department": "Development",
                "salary": 120000,
                "months": {
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
            },
            {
                "employee_ID": 103,
                "name": "Charlie Davis",
                "username": "charlie.d",
                "password": "Ch4rlieDev",
                "designation": "Employee",
                "department": "Testing",
                "salary": 75000,
                "months": {
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
            },
            {
                "employee_ID": 104,
                "name": "Dana White",
                "username": "dana.white",
                "password": "Dana@White",
                "designation": "Manager",
                "department": "Testing",
                "salary": 115000,
                "months": {
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
            },
            {
                "employee_ID": 105,
                "name": "Eva Green",
                "username": "eva.green",
                "password": "EvaG2024",
                "designation": "Employee",
                "department": "Design",
                "salary": 78000,
                "months": {
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
            },
            {
                "employee_ID": 106,
                "name": "Frank Hill",
                "username": "frank.h",
                "password": "Fr@nkHill",
                "designation": "Employee",
                "department": "Development",
                "salary": 87000,
                "months": {
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
            },
            {
                "employee_ID": 107,
                "name": "Grace Lee",
                "username": "grace.lee",
                "password": "Gr@c3L2024",
                "designation": "Employee",
                "department": "HR",
                "salary": 68000,
                "months": {
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
            },
            {
                "employee_ID": 108,
                "name": "Henry Ford",
                "username": "henry.f",
                "password": "HenryF@2024",
                "designation": "Manager",
                "department": "HR",
                "salary": 105000,
                "months": {
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
            },
            {
                "employee_ID": 109,
                "name": "Ivy Baker",
                "username": "ivy.baker",
                "password": "Iv!Baker2024",
                "designation": "Employee",
                "department": "Marketing",
                "salary": 74000,
                "months": {
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
            },
            {
                "employee_ID": 110,
                "name": "Jack Cooper",
                "username": "jack.cooper",
                "password": "J@ckC2024",
                "designation": "Employee",
                "department": "Support",
                "salary": 72000,
                "months": {
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
            },
            {
                "employee_ID": 111,
                "name": "Karen Young",
                "username": "karen.y",
                "password": "K@renY!2024",
                "designation": "Manager",
                "department": "Support",
                "salary": 110000,
                "months": {
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
            },
            {
                "employee_ID": 112,
                "name": "Leo Walker",
                "username": "leo.walker",
                "password": "LeoW@2024",
                "designation": "Employee",
                "department": "Development",
                "salary": 83000,
                "months": {
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
            },
            {
                "employee_ID": 113,
                "name": "Mia Roberts",
                "username": "mia.roberts",
                "password": "Mi@R2024",
                "designation": "Employee",
                "department": "Marketing",
                "salary": 76500,
                "months": {
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
            },
            {
                "employee_ID": 114,
                "name": "Nathan King",
                "username": "nathan.king",
                "password": "N@thanK2024",
                "designation": "Manager",
                "department": "Marketing",
                "salary": 118000,
                "months": {
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
            },
            {
                "employee_ID": 115,
                "name": "Olivia Martinez",
                "username": "olivia.m",
                "password": "Ol!viaM2024",
                "designation": "Employee",
                "department": "Design",
                "salary": 79500,
                "months": {
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
                    "dec": 22,
                }
            }
        ]

    def get_employee(self, employeeID):
        """Function will take employeeID as input and will return the employee whose employee ID is
        passes as parameter"""
        for item in self.__employees:
            if item['employee_ID'] == employeeID:
                return item

    def show_all_employees(self):
        """FUnction will print the details of all the employees"""
        global table
        table.field_names = ["employeeID", "names", "designation", "department"]
        employee_data = []
        for employee in self.__employees:
            employee_data.append([employee["employee_ID"],
                                  employee["name"],
                                  employee["designation"],
                                  employee["department"]])
        table.add_rows(employee_data)
        table.sortby = "department"
        print(table)

    def show_all_employees_full_attendance(self):
        """FUnction will print the details of all the employees"""
        employee_column = ["employeeID", "names", "designation", "department", "working days"]
        employee_rows = []
        for employee in self.__employees:
            employee_rows.append([employee["employee_ID"],
                                  employee["name"],
                                  employee["designation"],
                                  employee["department"],
                                  self.annual_attendance(employee["employee_ID"])])
        return [employee_column, employee_rows]

    def annual_attendance(self, employeeID):
        """function will return total working days of the year of a specific employee"""
        total_days = 0
        employee = self.get_employee(employeeID)
        for month in employee["months"]:
            total_days += employee["months"][month]
        return total_days

    def authenticate(self, uname, word):
        """function will authenticate the login details and will check for successful login"""
        for employee in self.__employees:
            if uname == employee["username"] and word == employee["password"]:
                if employee["designation"] == "Manager":
                    return [1, employee]
                else:
                    return [0, employee]
        return [-1, None]
