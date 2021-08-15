

'''
try:
    block of code which may raise exception
    risky code
except <OptionalError> :
    block of code when exception / error occurred
'''
''' 
Specific error first, generic error later
ChildClass first, parent class later
'''
try:
    list_test = [20,24,55]
    print(list_test[1])
    total_marks = int(input("Enter total marks"))
    obtained_marks = int(input("Enter obtained marks"))
    percentage = ((obtained_marks/total_marks) * 100)
    print("Your Percentage is {} ".format(percentage))
except (ZeroDivisionError, ValueError) as commonError:
    print("Invalid Input Provided", commonError)
except Exception as ex:
    print("Don't know which, but exception occurred", ex)
else:
    print("Try block completed successfully")
finally:
    print("Finally Executes regardless of error or not")
