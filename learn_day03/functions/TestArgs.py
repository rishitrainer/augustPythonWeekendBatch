def validate(name, cust_id, address, *args):
    validation_flag = True
    if not str(name).isalpha():
        validation_flag = False
    if not str(cust_id).isnumeric():
        validation_flag = False
    if not len(str(address)) >= 10:
        validation_flag = False

    for eachValue in args:
        print("Validating ", eachValue)
        if not str(eachValue).isalpha():
            validation_flag = False

    if not validation_flag:
        print("Validation Failed, Invalid Data Received")

    return validation_flag

validity = validate("David", 1200, "3375 Spring Hill Pwky", "332116", "Assam")
print("Validity", validity)