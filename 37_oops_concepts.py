"                                                       🐍 Basic Understanding of OOPs Concepts 🐍                                                                                                                                "

# OOPs:
'''
-> Object Oriented Programming is a fundamental concept in Python, empowering developers to build modular, maintainable, and scalable applications. 
-> By understanding the core OOP principles, programmers can leverage the full potential of Python OOP capabilities to design elegant and efficient 
   solutions to complex problems.
'''
# Types of OOPs:
'''
1. Class and Object
2. Inheritance
3. Polymorphism
4. Encapsulation
5. Data Abstraction
'''
# OOPs Terminologies:
'''
1. Variables / Attributes / Data Members
2. Functions / Methods / Behaviour
'''
# 1. Class and Object:
'''
Class : Logical Structure / Blueprint for creating Objects
Object : Physical Entity / Instance of Class
'''
# Self Parameter:
'''
-> self refers to the current instance of class
-> used to access variable that belongs to the class
'''
# __init__() method:
'''
-> called automatically everytime the class is being used to create a new object
-> use when you want to assign values to object properties, or other operations that are necessary to do when the object is 
   being created
'''

# e.g.,

class MyClass():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        print(a) # we cannot access like this in other method
        print(self.a)
    
    def my_function(self):
        print(self.a, self.b, self.c)

object = MyClass(1,2,3)
object.my_function()
# Output: 1
#         1
#         1 2 3

class MyClass():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_details(self):
        print(f"My name is {self.name}.")
        print(f"My age is {self.age}.")

object = MyClass("Kobe", 23)
object.print_details()
# Output: My name is Kobe.
#         My age is 23.

class MyClass():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_details(self):
        print(f"My name is {self.name}.")
        print(f"My age is {self.age}.")

object = MyClass("Kobe",23)
print(object.name)
# Output: Kobe
del object.name
# print(object.name)
# Output: AttributeError: 'MyClass' object has no attribute 'name'
print(object)
# output: <__main__.MyClass object at 0x0000020B9A4B0F80> 
del object

class MobilePhones():
    def __init__(self,company,model,ram,rom):
        self.a = company
        self.b = model
        self.c = ram
        self.d = rom
    
    def print_detals(self):
        print(f"Company: {self.a}")
        print(f"Model: {self.b}")
        print(f"RAM: {self.c}")
        print(f"ROM: {self.d}")

object = MobilePhones("Realme", "Realme GT 6T", "8GB", "128GB")
object.print_detals()
# Output: Company: Realme
#         Model: Realme GT 6T
#         RAM: 8GB
#         ROM: 128GB

# 2. Inheritance:
'''
-> Inheritance allows us to define a class that inherits all the methods and properties from another class.
-> Parent class is the class being inherited from, also called base class.
-> Child class is the class that inherits from another class, also called derived class.
'''
# Create a Parent Class: Any class can be a parent class, so the syntax is the same as creating any other class:

# Create a Child Class: To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
    
# e.g.,

class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
        
class Student(Person):
    pass

x = Student("Rama", "Krishna")
x.printname()
# Output: Rama Krishna

class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
        
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Student("Rama", "Krishna")
x.printname()
# Output: Rama Krishna

class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
        
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("Rama", "Krishna")
x.printname()
# Output: Rama Krishna

# Types of Inheritance:

# 1. Single Inheritance: One Parent and One Child

class Parent():
    def parent_method(self):
        print("this is parent class")

class Child(Parent):
    def child_method(self):
        print("this is child class")
        
obj = Child()
obj.parent_method()
obj.child_method()
# Output: this is parent class
#         this is child class

# 2. Multiple Inheritance: Multiple Parents and One Child

class Father():
    def father_method(self):
        print("this is father class")

class Mother():
    def mother_method(self):
        print("this is mother class")

class Child(Father, Mother):
    def child_method(self):
        print("this is child class")
        
obj = Child()
obj.father_method()
obj.mother_method()
obj.child_method()
# Output: this is father class
#         this is mother class
#         this is child class

# 3. Multi - Level Inheritance: Grandfather --> Father --> Child

class GrandFather():
    def grandfather_method(self):
        print("this is grandfather class")

class Father(GrandFather):
    def father_method(self):
        print("this is father class")

class Child(Father):
    def child_method(self):
        print("this is child class")
        
obj = Child()
obj.grandfather_method()
obj.father_method()
obj.child_method()
# Output: this is grandfather class
#         this is father class
#         this is child class

# 4. Hierarchial Inheritance: One Parent and Multiple Children(siblings)

class Parent():
    def parent_method(self):
        print("this is parent class")

class Child1(Parent):
    def child_method(self):
        print("this is child1 class")

class Child2(Parent):
    def child_method(self):
        print("this is child2 class")
    
obj1 = Child1()
obj1.parent_method()
obj1.child_method()
# Output: this is parent class
#         this is child1 class

obj2 = Child2()
obj2.parent_method()
obj2.child_method()
# Output: this is parent class
#         this is child2 class

# 3. Polymorphism:
'''
-> Polymorphism refers to methods/ functions/ operators with the same name that can be executed on many objects or classes.
'''
# Method Overloading:

# e.g.,

# Without default value
class MyClass():
    def my_function(self, a, b, c):
        print(a, b, c)

obj = MyClass()
obj.my_function(1, 2, 3)
# obj.my_function(1, 2)
# obj.my_function(1)
# obj.my_function()
# Output: 1 2 3
#         TypeError: MyClass.my_function() missing 1 required positional argument: 'c'

# With default value
class MyClass():
    def my_function(self, a = None, b = None, c = None):
        print(a, b, c)

obj = MyClass()
obj.my_function(1, 2, 3)
obj.my_function(1, 2)
obj.my_function(1)
obj.my_function()
# Output: 1 2 3
#         1 2 None
#         1 None None
#         None None None

# Method Overriding:

# e.g.,

# Without super() function
class MyClass():
    def my_function(self):
        print("this is parent class")

class MyClass2(MyClass):
    def my_function(self):
        print("this is child class")
        
obj = MyClass2()
obj.my_function()
# Output: this is child class

# With super() function
class MyClass():
    def my_function(self):
        print("this is parent class")

class MyClass2(MyClass):
    def my_function(self):
        print("this is child class")
        super().my_function()
obj = MyClass2()
obj.my_function()
# Output: this is child class
#         this is parent class

# Beacause of Polymorphism we can execute the same method for all below classes
class Vehicle():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")

class Car(Vehicle):
    def move(self):
        pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Titanic", "Touring 20")
plane1 = Plane("Boeing", "745")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
# Output: Ford
#         Mustang
#         Titanic
#         Touring 20
#         Sail!
#         Boeing
#         745
#         Fly!

# 4. Encapsulation:
# Public, Protected(_), Private(__)

# e.g.,

# Protected(_)
class GFather():
    def __init__(self, a):
        self._y = a
        print(self._y)

class Father(GFather):
    def my_function1(self):
        print(self._y)

class Child(Father):
    def my_function2(self):
        print("child", self._y)

obj = Child(12)
obj.my_function1()
obj.my_function2()
# Output: 12
#         12
#         child 12

# Private(__)
# class GFather():
#     def __init__(self, a):
#         self.__y = a
#         print(self.__y)

# class Father(GFather):
#     def my_function1(self):
#         print(self.__y)

# class Child(Father):
#     def my_function2(self):
#         print("child", self.__y)

# obj = Child(12)
# obj.my_function1()
# obj.my_function2()
# Output: 12
#         AttributeError: 'Child' object has no attribute '_Father__y'. Did you mean: '_GFather__y'?  

# 5. Data Abstraction: hiding

# e.g.,

from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
    
class Tesla(Car):
    def mileage(self):
        print("The mileage is 30 kmph")

class Suzuki(Car):
    def mileage(self):
        print("The mileage is 40 kmph")

class Duster(Car):
    def mileage(self):
        print("The mileage is 50 kmph")

class Reanault(Car):
    def mileage(self):
        print("The mileage is 60 kmph")

obj1 = Tesla()
obj1.mileage()

obj2 = Suzuki()
obj2.mileage()

obj3 = Duster()
obj3.mileage()

obj4 = Reanault()
obj4.mileage()
# Output: The mileage is 30 kmph
#         The mileage is 40 kmph
#         The mileage is 50 kmph
#         The mileage is 60 kmph
