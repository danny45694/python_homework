import csv
import traceback

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

rows = employees.get("rows", [])

names = [f"{row[0]} {row[1]}" for row in rows]
print("All Names:", names)

names_with_e = [name for name in names if "e" in name.lower()]
print("Names with 'e':", names_with_e)
