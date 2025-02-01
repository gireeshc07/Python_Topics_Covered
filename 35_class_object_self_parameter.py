"                                                🐍 Classes, Objects and Self Parameter in Python 🐍                                                                  "


# 📚 Class: Blueprint of the object

# Syntax: class ClassName():
#             pass

# 📚 Object: Instance of the class

# Syntax: object_name = ClassName()

# e.g.,

# class with print()
class MyClass():
    print("This is class.")
# Output: This is class.

class MyClass():
    print("This is class.")
print(MyClass)
# Output: This is class.
#         <class '__main__.MyClass'>

# class with variable
class MyClass():
    num = 10
    print(num)
    print("This is class.")
# Output: 10
#         This is class.

class MyClass():
    num = 10
    print("This is class.")
# print(num) 
# Output: This is class.
#         NameError: name 'num' is not defined. Did you mean: 'sum'?

# creating object
class MyClass():
    num = 10
    print("This is class")
object = MyClass()
print(object.num)
print(object)
print(type(object))
# Output: This is class.
#         10
#         <__main__.MyClass object at 0x000001A86A910410>
#         <class '__main__.MyClass'>

class MyClass():
    num = 10
object1 = MyClass()
object2 = MyClass()
print(object1.num)
print(object2.num)
# Output: 10
#         10

def my_function():
    print("This is function.")
my_function()
# Output: This is function.

# class with methods
class MyClass():
    def my_method():
        print("This is class method")
# my_method()
# Output: NameError: name 'my_method' is not defined

class MyClass():
    def my_method():
        print("This is class method")
object = MyClass()
# my_method()
# Output: NameError: name 'my_method' is not defined

class MyClass():
    def my_method():
        print("This is class method")
object = MyClass()
# object.my_method()
# Output: TypeError: MyClass.my_method() takes 0 positional arguments but 1 was given

class MyClass():
    def my_method(self):
        print("This is class method")
object = MyClass()
object.my_method()
# Output: This is class method

# self parameter:
# self refers to the current instance of class
# used to access variable that belongs to the class

def addition(a,b):
    c = a + b
    print("The sum of 'a' and 'b' is ", c)
addition(10, 20)
# Output: The sum of 'a' and 'b' is  30

class CalculateAddition():
    def add(self, a, b):
        c = a + b
        print("The sum of 'a' and 'b' is ", c)
object = CalculateAddition()
object.add(10,20)
# Output: The sum of 'a' and 'b' is  30

class CalculateAddition():
    d = 30
    def add(self, a, b):
        c = a + b + self.d
        print("The sum of 'a' and 'b' is ", c)
object = CalculateAddition()
object.add(10,20)

# class with attributes and methods
class StudentDetails():
    def get_details(self):
        name = "Kobe Bryant"
        age = 23
        gender = "male"
        print(f"My name is {name}.")
        print(f"My age is {age}.")
        print(f"My gender is {gender}.")

object = StudentDetails()
object.get_details()
# Output: My name is Kobe Bryant.
#         My age is 23.
#         My gender is male.

class StudentDetails():
    def get_details(self):
        object.name = "Kobe Bryant"
        object.age = 23
        object.gender = "male"
    
    def print_details(self):
        print(f"My name is {object.name}.")
        print(f"My age is {object.age}.")
        print(f"My gender is {object.gender}.")

object = StudentDetails()
object.get_details()
object.print_details()
# Output: My name is Kobe Bryant.
#         My age is 23.
#         My gender is male.

class StudentDetails():
    def get_details(self):
        self.name = "Kobe Bryant"
        self.age = 23
        self.gender = "male"
    
    def print_details(self):
        print(f"My name is {self.name}.")
        print(f"My age is {self.age}.")
        print(f"My gender is {self.gender}.")

object = StudentDetails()
object.get_details()
object.print_details()
# Output: My name is Kobe Bryant.
#         My age is 23.
#         My gender is male.

class StudentDetails():
    def get_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def print_details(self):
        print(f"My name is {self.name}.")
        print(f"My age is {self.age}.")
        print(f"My gender is {self.gender}.")

object = StudentDetails()
object.get_details("Kobe Bryant", 23, "male")
object.print_details()
# Output: My name is Kobe Bryant.
#         My age is 23.
#         My gender is male.

# without any methods
class StudentDetails():
    name = ""
    age = 0
    gender = ""
object1 = StudentDetails()
object1.name = "David Goggins"
object1.age = 30
object1.gender = "male"

print(f"My name is {object1.name}.")
print(f"My age is {object1.age}.")
print(f"My gender is {object1.gender}.")
# Output: My name is David Goggins.
#         My age is 30.
#         My gender is male.

# Area of a room
class AreaOfRoom():
    def get_measurements(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def find_area(self):
        area_of_room = self.length * self.breadth
        print(f"The are of the room is {round(area_of_room)}.")
object = AreaOfRoom()
object.get_measurements(45.6, 32.8)
object.find_area()
# Output: The are of the room is 1496.
