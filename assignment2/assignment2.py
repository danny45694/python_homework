import csv
import traceback
import os
import custom_module
import csv
from datetime import datetime

#Task 2: Read a CSV File
file_path = "C:/Users/danie/CTD/Python/python_homework/csv/employees.csv"

def read_employees():
    employee_data = {}
    rows = []

    try:
        with open(file_path, 'r') as data_file:
            csv_data = csv.reader(data_file)
            for i, row in enumerate(csv_data):
                if i == 0:
                    employee_data['fields'] = row
                else:
                    rows.append(row)
            employee_data["rows"] = rows
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

    return employee_data

employees = read_employees()



#Task 3: Find the Column Index
def column_index(string):
    return employees["fields"].index(string) 

employee_id_column = column_index("employee_id")



#Task 4: Find the Employee First Name
def first_name(rowNumber):
    columnNumber = column_index("first_name")
    employee_name = employees["rows"][rowNumber]
    return employee_name[columnNumber]


#Task 5: Find the Employee: a Function in a Function

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id , employees["rows"])) 
    return matches

#Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_names = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_names])
    return employees["rows"]

#Task 8: Create a dict for an Employee

def employee_dict(row):
    fields = employees["fields"][:]
    fields.remove("employee_id")
    row_values = row[1:]
    employee_dict = dict(zip(fields, row_values))
    return employee_dict

#Task 9: A dict of dicts, for All Employees

def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        employee_id = row[0]
        result[employee_id] = employee_dict(row)
    return result

#Task 10: Use the os Module

def get_this_value():
    return os.getenv("THISVALUE")


# Task11: Creating Your Own Module
def set_that_secret(string):
    custom_module.set_secret(string)

#Task 12: Read minutes1.csv and minutes2.csv

def read_csv_as_dict(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        result = {"fields": [], "rows": []}
        for i, row in enumerate(reader):
            if i == 0:
                result["fields"] = row
            else:
                result["rows"].append(tuple(row))  # convert list to tuple
        return result


def read_minutes():
    m1 = read_csv_as_dict("../csv/minutes1.csv")
    m2 = read_csv_as_dict("../csv/minutes2.csv")
    return m1, m2

minutes1, minutes2 = read_minutes()


#Task 13: Create minutes_set

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    combined = set1.union(set2)
    return combined

minutes_set = create_minutes_set()

#Task 14: Convert to datetime

def create_minutes_list():
    data_list = list(minutes_set)
    convert = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), data_list)
    return list(convert)
minutes_list = create_minutes_list()
print(minutes_list)


#Task 15: Sort the Minutes List

def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list))
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)
    return converted_list
