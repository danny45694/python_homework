

def type_converter(type_of_output):
    x = func(*args, **kwargs)
    return type_of_output(x)


@type_converter
def return_int():
    return 5

@type_converter
def return_string():
    return "not a number"

y = return_int()
print(type(y).__name__) # This should print "str"
try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!") # This is what should happen