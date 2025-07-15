# Write your code here.

# Task1: Hello
def hello():
    print("Hello!")

# Task2: Greet with a Formatted String
def greet(name):
    print(f"Hello, {name}!")

# Task3: Calculator
operation = ""
def calc(num1, num2, operation):
    if num2 == 0:
        return "You cannot divide by 0"
    if type(num1) or type(num2) is str:
        print("You cannot use letters")
    if operation == "multiply":
        return num1 * num2
    elif operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 + num2
    elif operation == "divide":
        return num1 / num2
    elif operation == "modulo":
        return num1 % num2
    elif operation == "power":
        return num1 ** num2
    elif operation == int_divide:
        return num1 // num2

#Task 4: Data Type Conversion
def data_type_conversion(value, conversion):
    if conversion == float:
        convertValue = float(value)
        return convertValue
    elif conversion == str:
        convertValue = str(value)
        return convertValue
    elif conversion == int:
        convertValue == int(value)
        return convertValue