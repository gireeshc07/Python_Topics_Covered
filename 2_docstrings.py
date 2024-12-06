
# Docstrings in Python:
'''
-> It stands for documentation strings.
-> A docstring is a special string literal used to document modules, functions, classes, or methods.
-> We can write well-documented, clean Python code using docstrings.
-> They play a vital role in making your code self-explanatory.
-> They are enclosed within triple single quotes (''' ''') or triple double quotes(""" """).
-> Unlike regular comments, docstrings are accessible at runtime via the help() function or the object’s __doc__ attribute.
'''

# Rules for Docstrings:
'''
-> The first statement of a function, class, or module must be a docstring; otherwise, it will be treated as a comment.
-> String literals are used to write docstrings, not hashtags.
-> Good Practice: Start with a capital letter and end with a period (.).
-> Tool Tip: Hovering the cursor over a function name in an IDE shows the docstring for that function.
'''

# Why Use Docstrings?
'''
-> Provide clear documentation for functions, classes, and modules.
-> Used to describe what the code does and how to use it.
-> Help other developers quickly understand how to use your code.
-> Accessible at runtime to retrieve details on objects, classes, or functions.
'''

# Docstring Examples:

# 1. Function Docstring:

def add_numbers(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int): The first number
    b (int): The second number

    Returns:
    int: The sum of the two numbers
    """
    return a + b

print(add_numbers.__doc__) # Access the docstring using help() or __doc__
# print(help(add_numbers))

# ️2. Class Docstring:

class Calculator:
    """
    A simple calculator class that performs basic operations.

    Methods:
    add(a, b): Returns the sum of a and b.
    subtract(a, b): Returns the difference of a and b.
    """

    def add(self, a, b):
        """Adds two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtracts the second number from the first."""
        return a - b

print(Calculator.__doc__) # Access the class docstring

obj=Calculator()
print(obj.__doc__)
print(obj.add.__doc__)
print(obj.subtract.__doc__)

print(Calculator.__doc__)
print(Calculator.add.__doc__)
print(Calculator.subtract.__doc__)

# print(help(obj))
# print(help(Calculator))
# print(help(obj.add))
# print(help(Calculator.subtract))

# 3. Module Docstring:
'''
-> A module-level docstring gives an overview of what the module offers.
-> It’s placed at the top of the Python file.'''

# i. User-defined Module:

# e.g.

"""
This module provides functions to perform mathematical operations.

Functions:
- add_numbers(a, b): Adds two numbers.
- subtract_numbers(a, b): Subtracts one number from another.
"""
# The above docstring must be placed at the top of the Python file, then use below statement to access them.
print(__doc__)

# ii. Built-in Module:

# e.g.

import math
print(math.__doc__)
print(math.sqrt.__doc__)

# print(help(math))
# print(help(math.sqrt))

# Types of Docstrings:
"""
1. Triple-Quoted Docstrings
2. Google Style Docstrings
3. Numpydoc Style Docstrings
4. One-Line Docstrings(' ' ' or " " ")
5. Multi-Line Docstrings
6. Indentation Docstrings
7. Docstrings in Classes 
"""

# Best Practices for Docstrings:
'''
-> Be concise: Explain what the function or class does without unnecessary details.
-> Use proper formatting: Follow consistent style (e.g., Google or NumPy docstring style).
-> Keep it updated: Make sure the docstring reflects any code changes.
-> Write in imperative tone: For example, say "Return the sum" instead of "This function returns the sum".
'''

# When to Use Docstrings vs. Comments:
'''
-> Docstrings: Use them for documenting functions, classes, and modules.
-> Comments: Use them for clarifying tricky parts of the code.
'''
