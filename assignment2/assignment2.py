import csv

file_path = "C:/Users/danie/CTD/Python/python_homework/csv/employees.csv"

def read_employees():
    emptyDict = {}
    try:
        with open(file_path, "w") as file:
            write = csv.writer(file)
            for row in employees:
                writer.writerow(row)
            print(f"csv file {file_path} was created")
        except FileExistsError:
            print("That file already exists!")