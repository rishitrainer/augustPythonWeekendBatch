hello = "Hello, World!, this is Strange"
age = "21"
# Python String are arrays of Characters
print(hello[0])
print(hello[6])
print(hello[7])
print(hello[0:4]) # [start_index : end_index+1]
print(hello[-1])
print(hello[7:])
# function
print("hello.upper()" , hello.upper())
print("hello.lower()" , hello.lower())
print("hello.islower()", hello.islower())
print("hello.capitalize()" , hello.capitalize())
print("age.isdigit()", age.isdigit(), age.isnumeric())
print(hello.split(","))
print(hello.find("World"))

# Try reversing a String in single statement