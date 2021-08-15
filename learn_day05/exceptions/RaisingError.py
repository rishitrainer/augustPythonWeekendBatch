from learn_day05.exceptions.CustomError import InvalidAgeError

def validate_age():
    is_valid_customer = False
    age = int(input("Enter Customer Age:"))
    if age >= 18:
        print("Customer can purchase")
        is_valid_customer = True
    else:
        print("Customer Cannot Purchase")
        is_valid_customer = False
        raise InvalidAgeError("Customer Age is Invalid for Purchase")
    return is_valid_customer


purchase_flag = validate_age()
print("Purchase Flag" , purchase_flag)