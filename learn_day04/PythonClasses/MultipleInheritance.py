from learn_day04.PythonClasses.TestClass import MyTestClass as MT


class Parent1:

    def __init__(self):
        print("Parent 1 Constructor")


class Parent2:

    def __init__(self):
        print("Parent 2 Constructor")


class ChildClass(Parent2, Parent1):

    def __init__(self):
        print("Child Class Constructor")
        super().__init__()


child = ChildClass()