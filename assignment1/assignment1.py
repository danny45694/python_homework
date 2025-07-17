# Write your code here.

# Task1: Hello
def hello():
    print("Hello!")


# Task2: Greet with a Formatted String
def greet(name):
    print(f"Hello, {name}!")

greet("Daniel")
# Task3: Calculator

def calc(num1, num2, operation="multiply"):
    if num2 == 0:
        return "You cannot divide by 0"
    if type(num1) or type(num2) is str:
        print("You cannot use letters")
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 + num2
    elif operation == "divide":
        return num1 / num2
    elif operation == "modulo":
        return num1 % num2
    elif operation == "power":
        return num1 ** num2
    elif operation == "int_divide":
        return num1 // num2
    else:
        return num1 * num2

#Task 4: Data Type Conversion
def data_type_conversion(value, conversion):
    try:
        if conversion == float:
            convertValue = float(value)
            return convertValue
        elif conversion == str:
            convertValue = str(value)
            return convertValue
        elif conversion == int:
            convertValue == int(value)
            return convertValue
    except TypeError:
        print(f"You can't convert {value} into a {type}.")

#Task 5: Grading System, Using args

def grade(*args):
    try:
        total = 0
        average = 0
        total += sum(args)
        numOfArgs = len(args)
        average = total / numOfArgs
    except ValueError:
        print("Invalid data was provided")

# Task 6: Use a For Loop with a Range
def repeat(string,count):
    returnString = ""
    for i in range(count):
        returnString = string + string
    return returnString

# Task 7: Student Scores, Using Kwargs

def student_scores(positional, **kwargs):
    for key, value in kwargs.items():
        pass

# Task 8: Titleize, with String and List Operations
def titleize(sentence):
    little_words = ["a", "on","an","the","of","and","is","in"]
    string = sentence.split()
    new_words = []
    for word in string:
        if word in little_words:
            modified_word = word.lower()
            new_words.append(modified_word)
        else:
            modified_word = word.capitalize()
            new_words.append(modified_word)
    result = " ".join(new_words)
    return result

#print(titleize("testing that this is working. a on an the of and" \
#"is in"))

#Task 9: Hangman, with more String Operations

def hangman(secret, guess):
    placeholder = ""
    display = []
    word_length = len(secret)
    for i in range(word_length):
        if guess in secret:
            display[i].append(guess)
        else:
            placeholder += "_"
    return display

print(hangman("titles", "t"))