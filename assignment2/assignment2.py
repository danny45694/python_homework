import csv
import traceback


file_path = "C:/Users/danie/CTD/Python/python_homework/csv/employees.csv"

def read_employees():
    result = {}
    rows = []

    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    result["fields"] = row
                else:
                    row.append(row)
            result["rows"] = rows
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

    return result    

def column_index(string):
    employee_id_column = employees["fields"].index(string) 
    return employee_id_column

def first_name(rowNumber):
     