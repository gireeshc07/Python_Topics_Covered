
# What is a Variable in Python?
'''
-> A variable in Python is a symbolic name associated with a value stored in memory. 
-> It acts as a reference or label for the memory location where data is stored, making programming easier by using 
   meaningful names instead of direct memory addresses. 
-> Variables can store any data type, and their type can change dynamically during runtime.
'''

# Syntax Example:
my_variable = 10  # Creating a variable and assigning a value to it.

# Key Components:
# 1. Variable Name (my_variable):
#    The name of the variable that acts as a reference or label for the stored value.
# 2. Assignment Operator (=):
#    Stores the value in memory and associates the variable name with it.
# 3. Value (10):
#    The data or object being assigned to the variable.

# Variables vs. Human Memory (Real-Time Comparison)

# Human Approach:
'''
You need to remember the result of 10 + 20:
1. Perform the calculation in your mind.
2. Recall the answer whenever needed.'''

# Computer Approach:
'''
1. Store 10 and 20 in memory.
2. Compute their sum and store it in another memory location.
3. Use a variable name (e.g., c) to reference the result.
The values of a and b are added together, resulting in 30, which is stored in the variable c.'''

# Code Implementation:
a = 10
b = 20
c = a + b
print(f"The sum is: {c}")

# How Memory Allocation Works Internally:
'''
-> Python treats everything as an object, which can be described as "Object-Oriented Storage." When you assign a value to 
   a variable, Python creates an object in memory and assigns a reference to it using the variable name. 
-> But for optimization purposes, Python reuses the same memory location for certain values within specific ranges 
   (e.g., integers from -5 to 256) through a process called interning.

Each object in memory possesses the following attributes:
-> Value: The actual data the object holds. You can retrieve it printing the variable
-> Type: The data type of the object, which determines what operations can be performed on it. You can check it using 
         the type() function.
-> ID: A unique identifier(Memory Address) for the object. You can retrieve it using the id() function.'''

# Real-Time Example of Memory Allocation:
a = 10
print(a) # Output: 10
print(type(a)) # Output: <class 'int'>
print(id(a)) # Output: 140720084093656

# Understanding Memory Management Internally:
'''
-> Python's memory management combines proactive strategies like interning with reactive ones such as garbage collection 
   to optimize memory usage and efficiency.'''
   
# 1. Value Interning:
'''
-> Value interning is a memory optimization strategy where Python reuses memory locations for objects with the same value 
   to conserve space and enhance performance. This is particularly applicable to immutable data types such as integers, 
   strings, and certain tuples.
-> For example, integers within the range -5 to 256 are interned by default. This means that multiple variables referencing 
   the same integer within this range will point to the same memory location.'''
   
# Example:
a = 10
b = 10
print(id(a), id(b))  # Same ID because Python reuses memory for small integer objects (interning)

# 2. Garbage Collection:
'''
-> Garbage collection is a process where Python automatically identifies and frees up memory that is no longer being used 
   by any variables. This ensures that unused objects do not consume memory indefinitely.'''

# Example of Memory Behavior:
a = 10
print(a)
print(id(a))

b = 5
print(b)
print(id(b))

c = 5
print(c)
print(id(c))

a = 5
print(a)
print(id(a))

# Explanation of the Example:
'''
1. When 'a' is assigned the value 10, an integer object with the value 10 is created, and 'a' references this object.
2. When 'b' is assigned the value 5, a new integer object with the value 5 is created, and 'b' references it.
3. When 'c' is assigned the value 5, Python checks if an integer object with the value 5 already exists in memory. Since 
   it falls within the interning range (-5 to 256), 'c' references the existing integer object, resulting in shared 
   memory usage.
4. When 'a' is reassigned the value 5, it points to the existing object, so the integer 10 remains in memory but is no 
   longer referenced. Python's garbage collector will eventually deallocate this memory to prevent waste.

-> Together, interning and garbage collection help Python manage memory efficiently, allowing developers to focus on 
   coding without worrying about low-level memory management details.'''

# Key Features of Python Variables

# 1. Dynamic Typing:
'''
-> Python is dynamically typed, which means that variables do not need to have their type declared explicitly. 
-> The type is inferred based on the value assigned to the variable at runtime. This feature enhances code flexibility 
   and readability by allowing variables to change types during execution.'''

# Example:
x = 10        # x is an integer
x = "Hello"   # Now x is a string
'''
Explanation: The variable x initially references an integer object 10. Later, it references a string object "Hello", 
demonstrating Python's ability to change data types dynamically.'''

# 2. No Explicit Declaration:
'''
-> In Python, you do not need to declare a variable's type beforehand, unlike statically-typed languages like C or Java. 
-> This makes Python code simpler and faster to write.'''

# Example in Python:
x = 10        # Declaration and initialization in one step

# Example in C (for comparison):
# int x = 10;   // Type must be declared explicitly

# 3. Assignment and Initialization:
'''
-> In Python, a variable is created when a value is assigned to it. This is different from some other languages where you
   need to declare the variable before assigning a value.'''

# Example:
a = 10        # 'a' is assigned an integer value
b = "Python"  # 'b' is assigned a string value

# 4. Flexible Assignment:
'''
-> Python allows multiple variables to be assigned values in a single line or a single variable to be assigned the same 
   value in one go. This feature makes it easy to write concise code.'''

# Examples:
# Assigning multiple values to multiple variables:
a, b, c = 1, 2, 3

# Assigning the same value to multiple variables:
x = y = z = "Same Value"

# 5. Case Sensitivity:
'''
-> Python variable names are case-sensitive, meaning a and A are considered distinct variables. This is an important 
   distinction to keep in mind when naming variables.'''

# Example:
a = 5
A = 10
print(a)  # Output: 5
print(A)  # Output: 10

# 6. Memory Management:
'''
-> Python efficiently manages memory using a combination of proactive strategies like interning and reactive strategies 
   such as garbage collection. '''

# Python Casting:
'''
-> Casting in Python refers to the explicit conversion of one data type into another.
-> Python, being a dynamically typed language, allows variables to hold values of any type without requiring prior type 
   declaration. 
-> However, there are scenarios where ensuring a specific type for a variable is necessary, and this is achieved through 
   casting.'''

# How Casting Works in Python:
'''
-> Python uses constructor functions for casting. These are built-in functions associated with data type classes 
   (e.g., int, float, str), allowing explicit type conversion.'''

# e.g.,
a = int(3)  # 3 (integer)
b = float(3)  # 3.0 (float)
c = str(3)  # '3' (string)

# Python's Object-Oriented Nature in Casting:
'''
-> Python is designed with object-oriented principles, meaning it treats everything as an object. This includes not only 
   complex data structures and user-defined types but also the basic or primitive data types like integers, floats, and 
   strings. This foundational design enables consistent and structured casting.'''

# 1. Classes Represent Data Types:
'''
-> int, float, and str are not keywords but classes in Python.
-> These classes define how data is stored, manipulated, and cast.'''

# Example:
print(type(3))  # Output: <class 'int'>
print(type(3.0))  # Output: <class 'float'>
print(type("3"))  # Output: <class 'str'> 
   
# 2. Constructor Functions:
'''
-> Methods of these classes are used for casting. 
-> For instance:
   - int() is a constructor function for the int class.
   - float() is a constructor function for the float class.
-> This is why conversion between data types is handled using constructor functions.'''

# 3. Methods and Attributes:
'''
-> Each class provides specific methods and attributes.
-> This means they have:
   - Attributes: Metadata or properties associated with the object.
   - Methods: Functions that operate on the object.
-> For example:
   - The str class has methods like .upper(), .lower(), and .strip() for string manipulation.'''

# Comparison with Other Languages
'''
Python:
-> Treats everything as an object, even primitive types.

C or C++:
-> In C or C++, primitive types like int or float are not objects. They are simple data types that do not have methods or 
   attributes. Operations on them are performed using functions or operators, not methods.
'''
# Why Use Casting?
'''
1. Enforcing Specific Data Types:
-> To ensure variables are of the desired data type for a specific operation.

2. Handling User Input:
-> Input values in Python are always treated as strings. Casting is necessary to convert them into integers or floats 
   for mathematical operations.

3. Preventing Errors:
-> Helps avoid errors caused by incompatible types.'''

# Example:
x = "10"
y = 2
# result = x * y  # TypeError: can't multiply a string with an integer
result = int(x) * y  # Proper casting avoids this error
print(result)  # Output: 20


# How to Retrieve Data from Variables?
'''
-> Python provides the following methods to retrieve details about variables:
1. print(variable): Outputs the value.
2. type(variable): Returns the data type of the variable.
3. id(variable): Provides the memory address of the variable.'''

# Example:
a = 10
print(a)          # Output: 10
print(type(a))    # Output: <class 'int'>
print(id(a))      # Output: 140717279611608
 
# Assignining Values to Variables:

# 1. Basic Assignment
# e.g.,
a = 10 # Assigns the value 10 to the variable 'a'
print(a) # Output: 10

# 2. Tuple Packing
'''
-> When multiple values are assigned to a single variable without parentheses, Python implicitly creates a tuple.'''
# e.g.,
a = 1, 2, 3, 4
print(a) # Output: (1, 2, 3, 4)

# 3. Independent Variable Assignments
# e.g.,
a = 5
b = 10
c = a + b
print(c) # Output: 15

# 4. Compound Assignment
# e.g.,
a = 10
a += 4
print(a)

# 5. Single Value to Multiple Variables
'''
-> In Python, you can assign the same value to multiple variables in one line.This is useful for initializing variables 
   with the same initial value.'''
# e.g.,
a = b = c = "hello"
print(a, b, c)  # Output: hello hello hello

# Explanation:
'''
-> A single string object "hello" is created in memory.
-> The variables 'a', 'b', and 'c' all reference the same memory location, meaning they point to the same object.
-> Reassigning one variable (e.g., `a = "world"`) creates a new object, leaving others unchanged.'''

# Additional Information:
'''
-> Assigning the same value to multiple variables is a quick way to set up default values.
-> Be cautious when assigning mutable objects (e.g., lists or dictionaries) to multiple variables, as changes to one 
   variable will affect the others since they will reference the same memory location.'''

# Immutable Objects:
'''
-> Assigning an immutable object (such as strings, integers, or tuples) to multiple variables doesn't affect other 
   variables when reassigned because immutable objects can't be changed in place. When an operation is performed on an 
   immutable object, a new object is created.'''
  
# e.g.1
# Assigning the same value to multiple variables
a = b = c = "hello"
print(a, b, c)  # Output: hello hello hello

# e.g.2
# Reassigning one variable doesn't affect the others because strings are immutable
a = "world"
print(a, b, c)  # Output: world hello hello

# Mutable Objects:
'''
-> Assigning a mutable object (such as lists, dictionaries, or sets) to multiple variables shares the same memory 
   reference, so changes made to one variable will be reflected in all others referencing the same object.'''

# e.g.1
# Assigning the same mutable object to multiple variables
a = b = c = [1, 2, 3]
print(a, b, c)  # Output: [1, 2, 3] [1, 2, 3] [1, 2, 3]

# e.g.2
# Modifying one variable affects all since they reference the same object
a[0] = 10
print(a, b, c)  # Output: [10, 2, 3] [10, 2, 3] [10, 2, 3]

# Copying: 
'''
-> For creating independent copies of mutable objects, use .copy() for shallow copies or copy.deepcopy() for deep copies 
   (from the copy module) when working with nested data structures.'''

# 6. Multiple Values to Multiple Variables in Python
'''
-> Python provides a concise way to assign values to multiple variables in one line using unpacking or parallel assignment.'''

# 1. Parallel Assignment
'''
-> Parallel assignment refers to assigning values to multiple variables in a single statement.This eliminates the need 
   for separate assignment statements.'''

# Basic syntax for parallel assignment
a, b, c = 10, 20, 30
print(a, b, c)  # Output: 10 20 30
'''
Explanation:
-> Python creates individual objects for the values 10, 20, and 30.
-> The variables 'a', 'b', and 'c' store references to these objects.'''

# Matching Number of Variables and Values
'''
-> When assigning values to variables, the number of variables on the left must match the number of values on the right. 
   If they don't match, Python raises a ValueError.'''

# Error Handling:

# Example of not enough values
try:
    a, b, c = 10, 20  # Raises ValueError: not enough values to unpack (expected 3, got 2)
except ValueError as e:
    print("Error:", e)
# Output: Error: not enough values to unpack (expected 3, got 2)

# Example of too many values
try:
    a, b, c = 10, 20, 30, 40  # Raises ValueError: too many values to unpack (expected 3)
except ValueError as e:
    print("Error:", e)
# Output: Error: too many values to unpack (expected 3)

# Managing Extra Values with the Asterisk (*)
'''
-> The asterisk (*) operator allows you to collect the "extra" values into a list. This is useful when the number of values 
   is variable or unknown.'''

# When there are extra values
a, b, *c = 10, 20, 30, 40
print(a, b, c)  # Output: 10 20 [30, 40]
'''
How it works:
- 'a' gets the first value (10).
- 'b' gets the second value (20).
- '*c' collects the remaining values ([30, 40]) into a list.'''

# When there are no extra values to pack
a, b, *c = 10, 20
print(a, b, c)  # Output: 10 20 []
'''
If there are no additional values to pack, the variable with the * operator will be assigned an empty list.'''

# 2. Unpacking
'''
-> Unpacking specifically involves extracting values from an iterable (like a list, tuple, or set) and assigning them to 
   variables in a single step. This is useful for breaking down collections into individual components.'''
   
# Packing a Collection
'''
-> When we create a collection such as a list or tuple, we normally assign values to it. This is called "packing" a 
   collection.'''
   
# e.g.,
numbers = [1, 2, 3]
print(numbers)  # Output: [1, 2, 3]

# Unpacking a Collection
'''
-> In Python, we can extract the values of a collection and assign them to variables. This is called "unpacking" a 
   collection.'''

# e.g.1
a, b, c = numbers
print(a, b, c)  # Output: 1 2 3

# e.g.2
a, b, c = "hai"
print(a, b, c)  # Output: h a i
'''
Explanation:
-> The string "hai" is unpacked, and its individual characters ('h', 'a', 'i') are assigned to 'a', 'b', and 'c', 
   respectively.'''

# Important Note: The number of variables must match the number of values in the collection. If not, Python raises a 
# ValueError. You can use the asterisk (*) operator to collect the remaining values as a list.

# e.g.1
numbers = [1, 2, 3, 4, 5]
a, *b = numbers
print(a, b)  # Output: 1 [2, 3, 4, 5]
'''
-> The first element (1) is assigned to 'a'.
-> The remaining elements ([2, 3, 4, 5]) are collected into 'b' as a list.'''

# e.g.2
*a, b = numbers
print(a, b)  # Output: [1, 2, 3, 4] 5
'''
-> The last element (5) is assigned to 'b'.
-> The preceding elements ([1, 2, 3, 4]) are collected into 'a' as a list.'''

# e.g.3
a, *b, c = numbers
print(a, b, c)  # Output: 1 [2, 3, 4] 5
'''
-> The first element (1) is assigned to 'a'.
-> The last element (5) is assigned to 'c'.
-> The middle elements ([2, 3, 4]) are collected into 'b' as a list.'''

# Unpacking with Different Iterable Types
'''
-> Unpacking can be done with other iterable types like tuples and sets, but it's essential to keep in mind that sets do 
   not maintain order, so unpacking a set will not preserve the order of the elements.'''

# Unpacking a tuple
numbers_tuple = (1, 2, 3)
a, b, c = numbers_tuple
print(a, b, c)  # Output: 1 2 3

# Unpacking a set (order may vary)
numbers_set = {1, 2, 3}
a, b, c = numbers_set
print(a, b, c) # Output may vary due to the unordered nature of sets
# Output: 1 2 3

# Swapping Values with Unpacking
'''
-> Unpacking is a simple way to swap the values of two variables without needing a temporary variable.'''

# Swapping values
a, b = 10, 20
print(a, b)  # Output: 10 20
a, b = b, a
print(a, b)  # Output: 20 10

# Unpacking Nested Structures
'''
-> Unpacking is useful for iterating through complex structures like lists of tuples.'''

# e.g.,
# Unpacking nested structures
nested = [(1, 2), (3, 4), (5, 6)]
for (a, b) in nested:
    print(a, b)
# Output:
# 1 2
# 3 4
# 5 6

# 7. Deleting Variables
# e.g.,
a = 5
del a
# print(a)  # Output: NameError: name 'a' is not defined

# Real-World Examples:

# Scenario 1: E-commerce Application

# Variables can represent customer data or product details in an online shopping app:
customer_name = "John Doe"
product_price = 299.99
discount = 0.1
final_price = product_price * (1 - discount)
print(f"Final Price for {customer_name}: ${final_price}")
# Output: Final Price for John Doe: $269.99100000000004

# Scenario 2: Bank Transactions

# Variables store account balances and transaction amounts:
account_balance = 1000
withdrawal = 200
account_balance -= withdrawal
print(f"Updated Balance: ${account_balance}")
# Output: Updated Balance: $800

# Differences Between Python and C Language Variables

'''
|         Feature        |            C Language                  |                        Python                          |
|------------------------|----------------------------------------|--------------------------------------------------------|
| Declaration            | Requires explicit declaration (int a;) | Declaration is implicit during assignment (a = 10)     |
| Data Type Enforcement  | Statically typed (int a = 5;)          | Dynamically typed (a = 5; a = "hello")                 |
| Semicolons             | Required to terminate statements       | Optional; used only when combining multiple statements |
| Example Assignment     | int a; a = 5;                          | a = 5                                                  |'''

# Best Practices for Variables

# 1. Use meaningful names for variables:
user_age = 25  # Good
x = 25         # Avoid

# 2. Follow naming conventions like snake_case:
first_name = "John"

# 3. Avoid using Python keywords or built-in function names:
# def = 10  # Invalid
sum = 5   # Avoid; shadowing built-in sum()

# 4. Limit the scope of variables to their intended use.
