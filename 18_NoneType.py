
# Special Literal None:
'''
-> In Python, "None" is a special data type that represents the absence of a value or a null value. It is often used to signify that a variable has no value or that a function does not return anything.
-> It is a special singleton object, meaning there is only one instance of None in a Python program.
-> You don't create "None" using a constructor because it's a built-in constant. The reason why "None" has no constructor is singleton in nature, represents the absence of value etc.
'''
# Characteristics of None:
'''
-> None is the only instance of the "NoneType" class.
-> It is immutable, case-sensitive, and one of the Python keywords.
-> It is not equivalent to False, 0 or an empty string (""). It is its own unique data type.
-> First letter should always be in capital, otherwise we get NameError.
'''
# e.g.;
a=None
print(a)
# Output: None
print(type(a))
# Output: <class 'NoneType'>

# Common usage of None:

# 1. Default Arguments: Often used as a default value for parameters in functions.
# 2. Return value: used to indicate that a function does not return a value explicitly.
# 3. Placeholder: useful as a placeholder when a variable is yet to be assigned a meaningful value.

# e.g,
def myFunc():
    print()
a=myFunc()
print(a)

def myFunc(a=None):
    print(a)
myFunc()
myFunc(30)

# Note: When checking if a variable is "None", use the identity operator "is" rather than "==", because "None" is a singleton.

# e.g.,

x=None
if x==None:
    print("x is None")
else:
    print("x is not None")

x=None
if x is None:
    print("x is None")
else:
    print("x is not None")

# -> This ensures that you are checking for the exact "None" object, not just any value that might be considered equivalent to "None".
