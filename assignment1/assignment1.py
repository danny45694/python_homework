# Write your code here.

# Task1: Hello
def hello():
    return("Hello!")


# Task2: Greet with a Formatted String
def greet(name):
    return(f"Hello, {name}!")

print(greet("James"))
# Task3: Calculator

def calc(num1, num2, operation="multiply"):
    if not isinstance(num1, (int,float)) or not isinstance(num2, (int, float)):
        return "You can't multiply those values!"
    
    if num2 == 0 and operation == "divide":
        return "You can't divide by 0!"
    
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
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
        if conversion == "float":
            convertValue = float(value)
            return convertValue
        elif conversion == "str":
            convertValue = str(value)
            return convertValue
        elif conversion == "int":
            convertValue = int(value)
            return convertValue
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {conversion}."    

#Task 5: Grading System, Using args

def grade(*args):
    try:
        for i in args:
            if not isinstance(i,(int,float)):
                raise ValueError
            
        total += sum(args)
        average = total / len(args)
        if average > 89:
            return("Grade A")
        elif average <= 89 and average >= 80:
            return("Grade B")
        elif average <= 79 and average >= 70:
            return("Grade C")
        elif average <= 69 and average >= 60:
            return("Grade D")
        elif average < 60:
             return("Grade F")
        
    except:
        return "Invalid data was provided"

print(grade(90,"nine",89,90,89))

# Task 6: Use a For Loop with a Range
def repeat(string,count):
    print(string, count)
    returnString = ""
    for i in range(count):
        returnString += string
    return returnString

print(repeat("string", 3))

# Task 7: Student Scores, Using Kwargs

def student_scores(mode, **kwargs):
    if mode == "best":
        bestStudent = max(kwargs, key=kwargs.get)
        return bestStudent
    elif mode == "mean":
        total = sum(kwargs.values())
        count = len(kwargs)
        return total / count
    else: 
        return "Invalid mode"
    
print(student_scores("best", Alice=90, Bob=85, Charlie=95))

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
    placeholder = "_"
    letters = list(guess)
    display = []
    for char in secret:
        if char in letters:
            display.append(char)
        else:
            display.append(placeholder) 
    return "".join(display)

print(hangman("alphabet", "ab"))

#Task 10: Pig Latin. Another String Manipulation Exercise

def pig_latin(string):
    vowels = ["a", "e", "i", "o", "u"]
    pigLatinWords = []
    words = string.split()

    for word in words:
        if word[0] in vowels:
            pig_word = word + "ay"
        elif word.startswith("qu"):
            pig_word = word[2:] + "quay"
        else:
            consonant_cluster = ""
            i = 0
            while i < len(word) and word[i] not in vowels:
                if word[i:i+2] == "qu":
                    consonant_cluster += "qu"
                    i += 2
                    break
                consonant_cluster += word[i]
                i += 1
            pig_word = word[i:] + consonant_cluster + "ay"
        
        pigLatinWords.append(pig_word)

    return " ".join(pigLatinWords)
