# Different types of variables

name = "Neil Armstrong" # String - class str
address = '3305 Spring Hill Pwky' # String in single quotes
age = 21 # integer class 'int'>
percentage = 99.14 # decimal - float class 'float'
complex_var = 1 + 5j  # class 'complex'
is_valid_customer = False # class 'bool'

print(name, type(name), id(name))
print(address, type(address), id(address))
print(age, type(age), id(age))
print(percentage, type(percentage), id(percentage))
print(complex_var, type(complex_var), id(complex_var))
print(is_valid_customer, type(is_valid_customer), id(is_valid_customer))

# Rules
age = 22
age23 = 23
# 24age = 24 # Cannot start with Number
age_44 = 44
# Case Sensitive
Age = 24
AGE = 25
print("age ", age)
print("Age ", Age)
print("AGE ", AGE)

# 256 characters are allowed as variables names
_ = "Koding Kings"
print(_)

__ = int("44")
print(__, type(__))



int_percent = int(percentage)
print(int_percent, type(int_percent))

str_age = str(age)
print(str_age, type(str_age))
# Constructor - initializer - for defining your own data type