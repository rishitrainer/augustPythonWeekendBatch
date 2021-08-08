def validate(name, cust_id, address, **kwargs):
    validation_flag = True
    if not str(name).isalpha():
        validation_flag = False
    if not str(cust_id).isnumeric():
        validation_flag = False
    if not len(str(address)) >= 10:
        validation_flag = False
    for key,value in kwargs.items():
        if key=="state":
            if not str(value).isalpha():
                validation_flag = False
        if key=="zipCode":
            if not ((len(str(value)) == 5) and (str(value).isnumeric())):
                validation_flag = False
    if not validation_flag:
        print("Validation Failed, Invalid Data Received")
    return validation_flag


validate("Niel", 1100, "Some Address in NASA", state="Florida", zipCode="A3639", country="United State")