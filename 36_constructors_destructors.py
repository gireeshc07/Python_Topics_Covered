"                                              🐍 Constructors and Destructors in Python 🐍                                                              "

# Constructors:
'''
-> The task of constructors is to assign values to the data members of the class when an object of class is created.
'''
# Types of constructor 1. Default constructor
#                      2. Parameterized constructor

# 1. Default Constructor:
# e.g.,

class Constuctor():
    def __init__(self):
        print("Python")
        
object = Constuctor()
# Output: Python

class StudentDetails():
    def __init__(self):
        name = "Kobe"
        age = 22
        print("My name is : ",name)
        print("My age is : ",age)
        
object1 = StudentDetails()
object2 = StudentDetails()
# Output: My name is :  Kobe
#         My age is :  22
#         My name is :  Kobe
#         My age is :  22

class Constructor():
    def __init__(self):
        print("This __init__ 1")
    
    def __init__(self):
        print("This __init__ 2")

object1 = Constructor()
object2 = Constructor()
# Output: This __init__ 2
#         This __init__ 2

# 2. Parameterized Constructor:
# e.g.,

class StudentDetails():
    def __init__(self, name, age):
        print("My name is : ",name)
        print("My age is : ",age)

object = StudentDetails("Kobe", 22)
# Output: My name is :  Kobe
#         My age is :  22

class StudentDetails():
    def __init__(self, name):
        age = 22
        print("My name is : ",name)
        print("My age is : ",age)

object = StudentDetails("Kobe")
# Output: My name is :  Kobe
#         My age is :  22

class StudentDetails():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_details(self):
        print("My name is : ",self.name)
        print("My age is : ",self.age)

object = StudentDetails("Kobe", 22)
object.get_details()
# Output: My name is :  Kobe
#         My age is :  22

class StudentDetails():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_details(self):
        print("My name is : ",self.name)
        print("My age is : ",self.age)

object = StudentDetails("Kobe", 22)
object.get_details()
object = StudentDetails("Goggins", 23)
object.get_details()
# Output: My name is :  Kobe
#         My age is :  22
#         My name is :  Goggins
#         My age is :  23

class StudentDetails():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_details(self):
        print("My name is : ",self.name)
        print("My age is : ",self.age)

object1 = StudentDetails("Kobe", 22)
object1.get_details()
object2 = StudentDetails("Goggins", 23)
object2.get_details()
# Output: My name is :  Kobe
#         My age is :  22
#         My name is :  Goggins
#         My age is :  23

# Types of Arguments in Parameterized Constructor:

# 1. Positional Arguments:
# e.g.,

class StudentDetails():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_details(self):
        print("My name is : ", self.name)
        print("My age is : ", self.age)

student1 = StudentDetails("Kobe", 22)
student1.get_details()
student2 = StudentDetails("Goggins", 23)
student2.get_details()
# Output: My name is :  Kobe
#         My age is :  22
#         My name is :  Goggins
#         My age is :  23

# 2. Keyword Arguments:
# e.g.,

class StudentDetails():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_details(self):
        print("My name is : ", self.name)
        print("My age is : ", self.age)

student1 = StudentDetails(name="Kobe",age=22)
student1.get_details()
student2 = StudentDetails(age=23,name="Goggins")
student2.get_details()
# Output: My name is :  Kobe
#         My age is :  22
#         My name is :  Goggins
#         My age is :  23

# 3. Default Arguments:
# e.g.,

class StudentDetails():
    def __init__(self, name, age=30):
        self.name = name
        self.age = age
    
    def get_details(self):
        print("My name is : ", self.name)
        print("My age is : ", self.age)

student1 = StudentDetails("Kobe",22)
student1.get_details()
student2 = StudentDetails("Goggins")
student2.get_details()
# Output: My name is :  Kobe
#         My age is :  22
#         My name is :  Goggins
#         My age is :  30

# 4. Variable Length Arguments: 1. Arbitrary Arguments(*args)
#                               2. Arbitrary Keyword Arguments(**kwargs)

# 1. Arbitrary Arguments(*args):
# e.g.,

class Sum():
    z = 0
    
    def __init__(self, x, *y):
        z = x
        for item in y:
            z = z + item
        print("Total: ", z)

object = Sum(10, 20, 30, 40, 50)
# Output: Total:  150

class Sum():
    def __init__(self, x, *y):
        for item in y:
            x = x + item
        print("Total: ", x)

object = Sum(10, 20, 30, 40, 50)
# Output: Total:  150

# 2. Arbitrary Keyword Arguments(**kwargs):
# e.g.,

class PersonalDetails():
    def __init__(self, name, **details):
        print("My name is: ", name)
        print("My age is: ", details["age"])
        print("My city is: ", details["city"])
        print("My phone number is: ", details["ph"])

object = PersonalDetails("Kobe Bryant", age = 22, city = "Washington", ph = "1234567890")
# Output: My name is:  Kobe Bryant
#         My age is:  22
#         My city is:  Washington
#         My phone number is:  1234567890

# Real-World Example:

# Area of Triangle
class AreaOfTriangle():
    def __init__(self, h, b):
        self.height = h
        self.base = b
    
    def find_area_of_triangle(self):
        area_of_triangle = 0.5 * self.height * self.base
        print(f"The are of triangle is {area_of_triangle}")

object = AreaOfTriangle(8,16)
object.find_area_of_triangle()
# Output: The are of triangle is 64.0

# Constructor with return statement
# e.g.,

class addition():
    def add(self, a, b):
        c = a + b
        return c
    
object = addition()
print(object.add(10, 20))
# Output: 30

# class addition():
#     def __init__(self, a, b):
#         c = a + b
#         return c
# object = addition(10, 20)
# Output: TypeError: __init__() should return None, not 'int'

# Constructor: It is called when object is created
# Destructor: It is called when object is destroyed

class Person:
    def __init__(self, name):  # Constructor
        self.name = name
        print(f"Object created for {self.name}")
    
    def __del__(self):  # Destructor
        print(f"Object destroyed for {self.name}")

# Creating an object
person1 = Person("Bob")
# Deleting the object
del person1

# Output: Object created for Bob
#         Object destroyed for Bob
