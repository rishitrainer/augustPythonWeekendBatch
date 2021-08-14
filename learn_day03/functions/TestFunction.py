'''
def - define a function
function - user defined function name - logical - rules similar to variable
inputs - options given in ()
block of code - indented
output - optional , provided by return
'''
def greet(name, language="English"):
    print("This is greet function block")
    if language == "English":
        print("Hello ", name)
    else:
        print("Namaste", name)


def sayHello(langauge="English"):
    name = input("Enter Your Name:")
    greet(name, langauge)


def square(number):
    sqr = number*number
    return sqr

# functions are instances and variables can assigned to their values
test_sqr = square
print(type(square))
print(test_sqr(10))


'''
greet("English", "David")
greet("David")
sayHello("Hindi")
sqr_test = square(5)
print(sqr_test)
'''