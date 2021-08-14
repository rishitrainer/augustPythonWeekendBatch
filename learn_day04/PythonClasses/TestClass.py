class MyTestClass:
    # variables
    age = 21
    name = "My Class Name"
    sample = 99.14

    # methods - instance methods
    def mysample_method(self):
        self.method_variable = 100
        print(self.sample, self.name)


    # methods = static methods - class methods
    # decorator @additional information
    @staticmethod
    def company_name():
        return "Koding Kings"


# Instance of class - Object
test1 = MyTestClass()
test2 = MyTestClass()

test2.age=50
test2.name="Neil"
test2.sample=55.66
test2.mysample_method()

print(type(test2.mysample_method))

'''
print(MyTestClass.company_name())

print(test1.name)
print(test1.age)
print(test1.sample)
test1.mysample_method()

print(test2.name)
print(test2.age)
print(test2.sample)
'''

