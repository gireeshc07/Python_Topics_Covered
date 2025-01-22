# Unpacking Operator in Pyhton:
'''
-> The unpacking operator * works by:
     - Deconstructing elements of an iterable into individual items.
     - Spreading these items into another context, such as lists, tuples, or function arguments.
'''
# e.g.,
numbers = [1, 2, 3]
print(*numbers)  # Output: 1 2 3

# Here, *numbers unpacks the list [1, 2, 3] into separate values 1, 2, and 3.

# Basic Syntax: *iterable
'''
-> The * operator is placed before the iterable you want to unpack.
'''

# Contexts Where It’s Used:
'''
1. Constructing new iterables.
2. Passing arguments to functions.
3. Assigning elements to variables.
4. Flattening nested structures.
'''
number = 42
*values, = number  # Raises TypeError
# TypeError: cannot unpack non-iterable int object
# SyntaxError: starred assignment target must be in a list or tuple

# Use Cases and Examples:

# 1. Constructing New Iterables: The unpacking operator makes it easy to combine or extend iterables.

# Combining Lists:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]
print(combined)  
# Output: [1, 2, 3, 4, 5, 6]

# Merging Different Iterables:
tuple1 = (7, 8, 9)
set1 = {10, 11, 12}
merged = [*tuple1, *set1]
print(merged)  
# Output: [7, 8, 9, 10, 11, 12]

# 2. Passing Arguments to Functions: 

# Positional Arguments with *:
# The unpacking operator can expand a list or tuple into positional arguments for a function.

def multiply(a, b, c):
    return a * b * c

args = [2, 3, 4]
result = multiply(*args)  # Equivalent to multiply(2, 3, 4)
print(result)  
# Output: 24

# Keyword Arguments with **: 
# The double unpacking operator ** works for dictionaries, expanding key-value pairs into keyword arguments.

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

info = {"name": "Alice", "age": 25}
greet(**info)  
# Output: Hello, Alice! You are 25 years old.

# 3. Unpacking During Assignments: The * operator allows you to unpack elements during assignment, often capturing remaining values in a list.

# List Unpacking:
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)   
# Output: 1
print(middle)  
# Output: [2, 3, 4]
print(last)    
# Output: 5

# String Unpacking:
word = "Python"
first, *middle, last = word
print(first)   
# Output: P
print(middle)  
# Output: ['y', 't', 'h', 'o']
print(last)    
# Output: n

# 4. Flattening Nested Iterables: When working with nested lists, the unpacking operator can simplify the process of flattening them.

nested = [[1, 2], [3, 4], [5, 6]]
flattened = [*nested[0], *nested[1], *nested[2]]
print(flattened)  
# Output: [1, 2, 3, 4, 5, 6]

# 5. Splitting Data Dynamically: The * operator is useful for splitting data dynamically, especially when the size of the data is not predetermined.

data = [10, 20, 30, 40, 50]
head, *body, tail = data
print(head)  
# Output: 10
print(body)  
# Output: [20, 30, 40]
print(tail)  
# Output: 50

# Advantages:
'''
-> Improves Code Readability: Simplifies handling of iterables without complex loops or temporary variables.
-> Flexible and Dynamic: Adapts to iterables of varying sizes and structures.
-> Supports Multiple Iterables: Works seamlessly across different types like lists, tuples, sets, and dictionaries.
-> Facilitates Argument Passing: Makes passing arguments to functions cleaner and more concise.
'''

# Limitations:
'''
-> Not Suitable for Non-Iterable Objects: Attempting to unpack a non-iterable object like an integer or a None value will result in a TypeError.
'''

number = 42
*values, = number  # Raises TypeError

# One-Level Unpacking Only: The unpacking operator doesn’t handle nested structures automatically.
nested = [[1, 2], [3, 4]]
flattened = [*nested]  
# Output: [[1, 2], [3, 4]]

# Alternative Approaches:
'''
If the unpacking operator isn’t suitable or available, similar results can be achieved using loops or comprehensions.
'''

# Flattening Nested Lists with a Loop:
nested = [[1, 2], [3, 4], [5, 6]]
flattened = []
for sublist in nested:
    flattened.extend(sublist)
print(flattened)
# Output: [1, 2, 3, 4, 5, 6]

# Using List Comprehension:
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print(flattened)  
# Output: [1, 2, 3, 4, 5, 6]
