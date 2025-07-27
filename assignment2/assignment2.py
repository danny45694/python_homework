import csv
import traceback

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
    sorted_names = employees["rows"].sort(key=lambda row: row[last_names])
    return sorted_names

print(sort_by_last_name())