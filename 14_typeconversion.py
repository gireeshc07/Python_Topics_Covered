
# Type Conversion in Python:
'''
-> The process of converting one data type to another data type is called "Type Conversion".'''

# Types of Type Conversion in Python:
'''
Python provides two primary types of type conversion:

1. Implicit Type Conversion (Type Coercion)
2. Explicit Type Conversion (Type Casting)
'''
# Implicit Type Conversion (Type Coercion):
'''
-> Implicit type conversion occurs when Python automatically converts one data type to another without requiring any explicit action from the programmer. 
-> This process is also called type coercion or automatic type conversion.
'''
# Key Characteristics of Implicit Type Conversion:

# 1. Automatic Conversion: Python handles type conversion automatically during operations.

# 2. No Data Loss: Python ensures no loss of data during the conversion. It typically converts smaller types to larger or more general types (e.g., integers to floats).

# 3. Developer-Friendly: Reduces the need for manual type casting, simplifying the code.

# 4. Context-Specific: Occurs only in situations where it's safe and logical (e.g., arithmetic operations involving different types).

# Limitations of Implicit Conversion:

# 1. Unexpected Behavior: Implicit conversion can sometimes produce results that are not intuitive.
   
# e.g.,
x = True + False  # True is 1, False is 0
print(x)  # Output: 1

# 2. Does Not Handle All Scenarios: Implicit conversion is limited to safe and logical contexts. For instance:

# e.g.,
x = "10"
y = 5
# result = x + y  # TypeError: unsupported operand types for +: 'str' and 'int'
 
# Explicit Type Conversion (Type Casting):
'''
-> Explicit type conversion allows the programmer to manually convert data from one type to another. It is done using Python's built-in type conversion functions.
-> This process is also called type casting or manual type conversion.
'''
# Key Characteristics of Explicit Type Conversion:

# 1. Manual Conversion: Performed by the programmer using specific functions.

# 2. Control: Gives full control over how data is transformed.

# e.g.,
pi=3.14159
print(round(pi)) # Rounding the float
# Output: 3
print(int(pi)) # Truncating the float
# Output: 3

# 3. Risk of Errors: Incorrect or invalid conversions can raise exceptions.

# 4. Data Loss: In explicit type conversion there is a possibility of data loss because we are forcing an expression to be converted into a specific data type (e.g., converting float to int).

# e.g.,
a=3.14
b=int(a)
print(b)
# Output: 3

a=0.59
b=int(a)
print(b)
# Output: 0

# Built-in Functions for Explicit Conversion:
'''
int()    -->   Converts to Integer                      
float()  -->   Converts to  Floating-point number        
str()    -->   Converts to  String                       
bool()   -->   Converts to Boolean                     
list()   -->   Converts to List                        
tuple()  -->   converts to  Tuple                        
set()    -->   Converts to  Set                         
dict()   -->   Converts to Dictionary
'''
# When to Use Explicit Type Conversion:

# 1. Converting User Input: User input is always a string. We should convert it into the required type for calculations.

# e.g.,
# age = input("Enter your age: ")  # String
# age = int(age)                   # Convert to integer
     
# 2. Ensuring Compatibility: Convert data types to avoid errors in operations.

# e.g.,
result = int(10.5) + int("5")
print(result)  # Output: 15
     
# 3. Working with Data Structures: Convert between lists, tuples, sets, and dictionaries as needed.

# 4. Type-Specific Operations: Explicit conversion ensures data is in the correct format for operations like indexing, slicing, or mathematical calculations.

# Risks and Considerations:

# 1. Invalid Conversions: Attempting to convert incompatible data types can result in errors.

# e.g.,
# This will raise an error
# print(int("hello"))  # ValueError
# Output: ValueError: invalid literal for int() with base 10: 'hello'

# 2. Data Loss: Conversions like float to int may truncate decimal parts.

# e.g.,
print(int(5.8))  # Output: 5

# 3. Unhashable Objects: Converting mutable types (e.g., lists) to unhashable types can raise errors in specific contexts.

# The following are some of the built-in functions for type conversion:

# 1.int():
'''
-> The int() function returns an integer by converting the specified value.
-> It returns 0 if no values are given.'''

# e.g.,
a=6.9;b=int(a);print(b)
a="123";b=int(a);print(b)
a=int();print(a)
''' 
-> Note that Python will raise ValueError message if you pass a value to int() function that it cannot convert to an integer.'''
 
# e.g.,
# a=int("1.23")
# print(a)
# b=int("Nine")
# print(b)

# 2.float():
''' 
-> The float() function returns a floating-point number by converting an integer or a string value. 
-> It returns 0 if no values are given.'''

# e.g.,
a=9;b=float(a);print(b)
a="1";b=float(a);print(b)
a="1.23";b=float(a);print(b)
a=float();print(a)
# a="4j";b=float(a);print(b)

# 3.complex():
''' 
-> The complex() function returns a complex number by converting a number or a string value.
-> Note that we cannot convert a complex type into another type.
-> This function takes two arguments. The first argument is a real number, and the second argument is an imaginary number.
-> It returns a complex number with the value ( real + imaginary ).'''

# Syntax: complex ( real, imaginary )

# e.g.,
a=complex(2,3);print(a)
a=complex(5.2,3);print(a)
a=complex(2.5,3.9);print(a)
''' 
-> if an imaginary part is omitted, it sets to zero.'''

# e.g.,
a=complex(9);print(a)
a=complex(2.5);print(a)
''' 
-> If both arguments are omitted, then it returns 0j.'''

# e.g.,
a=complex()
print()
''' 
-> The complex function also converts a string to a complex number.
-> If the first argument is a string, the function must be called without a second argument because the string will be considered as a complex number. 
-> A string is never allowed as the complex function's second argument.'''

# e.g.,
a=complex("9");print(a)
a=complex("3+2j");print(a)
# a=complex("9",3);print(a)
# a=complex(2,"3j");print(a)

# 4. str():
''' 
-> The str() function returns a string version by converting the specified value.
-> It returns an empty string if no values are given.'''

# e.g.,
a=9;b=str(a);print(b)
a=9.5;b=str(a);print(b)
a=(2+3j);b=str(a);print(b)
a=True;b=str(a);print(b)
a=False;b=str(a);print(b)

# 5. bool():
''' 
-> The bool() function returns a boolean value, i.e., True (or) False, by converting the specified value. 
-> If no argument is passed, then it returns False.
-> Almost any value is evaluated to True in bool() function if it has some sort of content.
-> Any string is True, except empty strings.
-> Any number is True, except 0.
-> Any iterable object is True, except empty one.'''

# e.g.,
# Values which evaluates to False
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(0+0j))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))
print(bool())

# Values which evaluates to True
print(bool(True))
print(bool(1))
print(bool(1.0))
print(bool(1+0j))
print(bool("1"))
print(bool([1]))
print(bool((1,)))
print(bool({1:2}))
print(bool({1}))

# int() revisited:
''' 
-> The int() function can also convert numbers that are given in other bases, such as binary,octal, or hexadecimal, to integers.'''

# Syntax: int(x,base)
'''
-> Here, x is a number in string form that are binary,octal and hexadecimal which can be optionally prefixed with "0b/0B, 0o/0O, 0x/0X", respectively.
-> Base: Base may be 2,8 or 16 for binary, octal and hexadecimal. By default, it is 10 for the decimal.'''

# e.g.,
a=int("0b11",2)
print(a)

a=int("11",2)
print(a)

a=int("0o12",8)
print(a)

a=int("12",8)
print(a)

a=int("0x12",16)
print(a)

a=int("12",16)
print(a)
'''  
-> Python will show an error message if you pass a value to int() that if cannot convert to an integer.'''

# e.g.,
# a=int("0b11",8)
# print(a)

# Some More Examples

a="Hello World";print(a)
# Output: Hello World
a=str(a);print(a)
# Output: Hello World

a=20;print(a)
# Output: 20
a=int(a);print(a)
# Output: 20

a=20.5;print(a)
# Output: 20.5
a=float(a);print(a)
# Output: 20.5

a=1j;print(a)
# Output: 1j
a=complex(1j);print(a)
# Output: 1j

a=range(6);print(a)
# Output: range(0, 6)

a=["apple","banana","cherry"];print(a)
# Output: ['apple', 'banana', 'cherry']
a=list(a);print(a)
# Output: ['apple', 'banana', 'cherry']

a=("apple","banana","cherry");print(a)
# Output: ('apple', 'banana', 'cherry')
a=tuple(a);print(a)
# Output: ('apple', 'banana', 'cherry')

a={"apple","banana","cherry"};print(a)
# Output: {'banana', 'apple', 'cherry'}
a=set(a);print(a)
# Output: {'banana', 'apple', 'cherry'}

a={1:"apple",2:"banana",3:"cherry"};print(a)
# Output: {1: 'apple', 2: 'banana', 3: 'cherry'}
a=dict(a);print(a)
# Output: {1: 'apple', 2: 'banana', 3: 'cherry'}

a=frozenset({"apple","banana","cherry"});print(a)
# Output: frozenset({'banana', 'apple', 'cherry'})
a=frozenset(("apple","banana","cherry"));print(a)
# Output: frozenset({'cherry', 'banana', 'apple'})

a=True;print(a)
# Output: True
a=bool(1);print(a)
# Output: True

a=b"Hello";print(a)
# Output: b'Hello'
a=bytes(5);print(a)
# Output: b'\x00\x00\x00\x00\x00'

a=bytearray(5);print(a)
# Output: bytearray(b'\x00\x00\x00\x00\x00')

a=memoryview(bytes(5));print(a)
# Output: <memory at 0x000001869979C940>

a=None;print(a)
# no constructor for NoneType
# Output: None

# Real-Life Analogy:

# 1. Implicit Conversion: Think of this as a smartphone automatically adjusting screen brightness based on ambient light. You don’t have to do anything; it just works.

# 2. Explicit Conversion: It’s like manually changing the brightness setting to suit your preference. You have full control, but you must know what you’re doing.

# Conclusion:
'''
Type conversion is a powerful feature in Python that ensures compatibility between data types. Implicit conversion is safe and automatic, while explicit conversion offers flexibility at the 
cost of potential errors. Always validate input and output when performing explicit conversions to avoid unexpected behavior.
'''
