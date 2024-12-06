
# print() function:
'''
-> It prints the given object on a device's screen. It directs the output to the console, displaying text on your terminal screen.
-> It is versatile and can handle various types of objects. When you pass an object to print(), it converts the object to a string representation 
   before displaying it. This is possible due to the __str__() method, which is defined in Python's base object class and can be overridden by 
   user-defined classes. If the object is already a string, it is printed as it is.'''
   
# Steps:
'''
1. Convert to String: The function converts each object to a string, applying the __str__() method where necessary.
2. Direct Output: Sends the formatted output to the specified destination (typically the console but customizable through the file parameter).'''

# Parameters in print() function: They control how output is formatted and displayed.

# Syntax: print(*objects , sep=" " , end="\n" , file="sys.stdout" , flush=False)

# 1. *Objects(required):
'''
-> These are the values you want to print.
-> We can pass multiple items separated by commas which can be Datatypes, Identifiers of Python, Function call, Instances of class etc.

*objects: If we specify asterisk(*) before any variable, we call it as variable length arguments. In print() function, the asterisk is not directly 
          used, but print() accepts a variable number of arguments. These are passed to print() as *objects, allowing you to print multiple items 
          at once.

e.g.'''

print("Hello World") # "Hello World" is framed by Brian Kernighan in his book C programming language in 1970.

name, age = "Alice", 30
print("Name:", name, "Age:", age)

# 2. sep=" "(optional):
'''
-> It specifies the separator b/w the objects.
-> By default, it is a single space(" ").

e.g.'''

print("apple", "banana", "cherry") # Default space separator 
print("apple", "banana", "cherry", sep=" - ") # Custom separator 
print("apple", "banana", "cherry", sep="") # No separator

# 3. end="\n"(optional):
'''
-> It specifies what is printed at the end of the output.
-> By default, it is a newline character(\n), which means each print call will move to a new line.
-> You can change it to other characters or an empty string if you want to continue the same line.

e.g.'''

print("Hello World")
print("Welcome to Python")

print("Hello World" , end="")
print("Welcome to Python")

print("Hello World" , end="\n\t")
print("Welcome to Python")

print(*["a","b",1,2])

# 4. file="sys.stdout"(optional):
'''
-> It specifies the file like object to which the output should be sent.
-> By default, it is sys.stdout, which means the output goes to the console.
-> You can redirect it to a file or other streams.

e.g.'''

print("Hello World","Welcome to Python") # output goes to the console

file_object=open("file_object.txt","w")
print("Hello World","Welcome to Python",file=file_object) # output is redirected to the specified text file
file_object.close()

# 5. flush=False(optional):
'''
-> It determines whether the output is flushed immediately or buffered.

   flush=False(default value) --> buffered (Python buffers out until the buffer is full or the program ends)
   flush=True --> flushed (When you need to see the output immediately)'''

# Buffering:
'''
-> When we print something, it doesn’t go directly to the terminal or file. Instead, it first goes to a temporary storage area called a buffer. 
   The output is displayed only when the buffer is full or flushed. This buffering occurs for some efficiency reasons, because writing to output 
   devices can be slow.'''

# Flushing:
'''
-> The flush parameter tells Python to force the contents of the buffer to be written out immediately, even if the buffer isn't full. This is 
   helpful in situations where you need to see output in real-time, such as when tracking progress or debugging.
-> If we include the newline character(\n) in print() function, it flushes the buffer automatically even without [flush=True].

e.g.'''

from time import sleep
for i in range(10):
    print(i, end=" ",flush=False)
    sleep(0.5)
print()

from time import sleep
for i in range(10):
    print(i, end=" ",flush=True)
    sleep(0.5)
print()

from time import sleep
for i in range(10):
    print(i, end="\n")
    sleep(0.5)
    
from time import sleep
for i in range(10):
    print(i,"\n")
    sleep(0.5)

# input() function:
'''
-> We use the input() function to take input from the user at runtime.
-> It treats the given data as a string.
-> Type conversion is needed if we want to perform any mathematical operations on the user input.
-> In Python 2.7, the method used was raw_input(), whereas in Python 3.6, it is input().
-> Python stops executing when it comes to the input() function, and continues when the user has given some input.

e.g. '''

# username=raw_input("Enter username: ") # not working in Python 3.6 and above versions
# print(username) 

username=input("Enter username: ")
print("username is: ",username)

# input() function vs print() function:

'''
| input() function                         | print() function                                 |
|------------------------------------------|--------------------------------------------------|
| 1. To take user input at runtime.        | 1. To display the output.                        |
| 2. Similar to scanf in C language        | 2. Similar to printf in C language               |
| 3. Inherently, it treats the given data  | 3. It takes the object, converts it to a string, |
|    as a string.                          |    and sends the output directly to the console. |
'''

# Python Modules:
'''
-> A module in Python is like a code library – A file that contains a set of functions and variables that you can use in your applications or 
   programs.
-> In simple terms, a module is nothing but a Python file. 
-> It has two types:'''

# 1. Pre-defined modules:
'''
-> These are modules already created by Python developers. They contain ready-made functions.
-> You can’t modify these modules.
-> Functions or methods in these modules are called pre-defined functions or built-in functions.'''

# 2. User-defined modules:
'''
-> A user-defined module is a .py file that a programmer creates to store custom functions, class or variables.
-> These modules can be imported, used, and modified in any way you like.
-> Functions or methods in these modules are called user-defined functions or custom functions.'''

# Built-in functions or methods:
'''
-> Python also has many built-in functions that can be used directly without importing anything. Some popular ones are:

e.g.'''

a=10
print(a) # displays output on the screen
print(type(a)) # tells you the data type of a variable
print(id(a)) # shows the memory address of a python object
print(len("hi")) #only iterable objects have the length

print(min(4,6,3,6)) # returns lowest value
print(max(4,6,3,6)) # returns largest value
print(abs(-45)) # returns positive value of a specified number
print(pow(10,2)) # X to the power of Y
print(sum(5,6)) # adds up all elements in an iterable
print(round(4.56864,2)) # used to round  a float to a specific no. of decimal places
print(divmod(9,2)) # returns a tuple of quotient & remainder
print(bin(10)) # to convert integer to its binary string representation
print(oct(10)) # to convert integer to its octal string representation
print(hex(10)) # to convert integer to its hexadecimal string representation
print(ord("a")) # returns the Unicode Code Point for a given character
print(input())# gets input from the user