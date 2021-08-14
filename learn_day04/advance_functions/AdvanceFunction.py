from learn_day03.functions.TestFunction import greet


def shout(text):
    return str(text).upper()

caps = shout
print(caps("I want this in Caps"))

def calculator(number, operation):
    function_name = None

    def square():
        return number*number

    def cube():
        return number*number*number

    if operation == "square":
        function_name = square
    else:
        function_name = cube

    return function_name

func_name = calculator(5, "cube")
print(func_name())
print(greet("English"))

# Function is instance of function class
# You can assign a Variable to function
# you can have function within a function (nested)
# You can return a function from a function