
# Python Indentation:
'''
-> Indentation refers to the spaces at the beginning of a code line.
-> Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
-> Python uses indentation to indicate a block of code.

e.g. '''

if 5>2:
    print("Yes")
    
'''
-> Python will give you an error if you skip the indentation.

e.g. '''

# if 5>2:
# print("Yes") # IndentationError will raise

'''
-> The no. of spaces is up to you as a programmer, the most common use is four, but it must be at least one.

e.g. '''

if 5>2:
    print("Yes")
if 5>2:
    print("No")
    
'''
-> You must use the same no. of spaces in the same block of code, otherwise Python will give you an error.

e.g. '''

# if 5>2:
#     print("Yes")
#         print("No")  # IndentationError will raise


# Python Keywords:
'''
-> Python has a set of keywords that are reserved words that have special meanings and purposes. 
-> They cannot be used as identifiers (like variable names, function names, etc.) because they are integral to the syntax and structure of the 
   language. 
-> Therefore, Keywords are essential for defining the syntax and structure of Python code. Understanding them is crucial for programming 
   effectively in Python.
-> As of the latest version, Python has 35 keywords.'''

# Here’s a list of Python keywords, along with a brief description of each:

# Keyword	                 Description
'''
and                   	A logical operator
as                    	To create an alias
assert                	For debugging
async	                Indicates that a function is asynchronous.
await	                Used to call an asynchronous function.
break                 	To break out of a loop
class                 	To define a class
continue              	To continue to the next iteration of a loop
def                   	To define a function
del                   	To delete an object
elif  	                Used in conditional statements, same as else if
else	                Used in conditional statements
except	                Used with exceptions, what to do when an exception occurs
False	                Boolean value, result of comparison operations
finally	                Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for                   	To create a for loop
from                  	To import specific parts of a module
global                	To declare a global variable
if                    	To make a conditional statement
import                	To import a module
in                    	To check if a value is present in a list, tuple, etc.
is                    	To test if two variables are equal
lambda	                To create an anonymous function
None                  	Represents a null value
nonlocal              	To declare a non-local variable
not                   	A logical operator
or                    	A logical operator
pass                  	A null statement, a statement that will do nothing
raise                 	To raise an exception
return                	To exit a function and return a value
True                  	Boolean value, result of comparison operations
try                   	To make a try...except statement
while                 	To create a while loop
with 	                Used to simplify exception handling
yield	                To return a list of values from a generator
'''

# Python Punctuators:
'''
-> A punctuator is a token. Some characters in Python are used as punctuators, which have syntactic and semantic meaning to the compiler.
e.g.

' " # /\ () [] {} ; : etc. '''
