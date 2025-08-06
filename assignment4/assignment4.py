import pandas as pd
import numpy as np
import json

data = [1, 3, 5, 7, 9]
s = pd.Series(data, name="numbers")
#print(s)

data = {"name": ['Alice', 'Bob','Charlie'],
 "Age":[25, 30, 35],
 "City": ['New York', 'Los Angeles','Chicago']
}

df = pd.DataFrame(data)
#print(df)
task1_data_frame = df

task1_with_salary = df.copy(deep=True)

task1_with_salary['Salary'] = [70000, 80000, 90000]
#print(task1_with_salary)

task1_older = task1_with_salary.copy(deep=True)
for entry in range(len(task1_older)):
    task1_older["Age"] = task1_older["Age"] + 1
print(task1_older)

task1_older.to_csv("employees.csv", index=False)

file_path = "employees.csv"
task2_employees = pd.read_csv(file_path)

json_data = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]
with open("additional_employees.json", "w") as f:
    json.dump(json_data, f)

json_employees = pd.read.json("additional_employees.json")
print(json_employees)

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
