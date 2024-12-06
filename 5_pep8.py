
# PYTHON PEP8
# PEP8:
'''
•	PEP8, short for Python Enhancement Proposal 8, is a style guide designed to help Python programmers write code that is 
    clean, consistent, and easy to read. 
•	It offers practical guidelines on how to format and structure your code so that it looks neat and is easier for others 
    to understand and maintain.'''
    
# Key PEP8 Recommendations:

# 1. Naming Conventions:
'''
•	Variables, functions, and methods: Use lowercase_with_underscores.
•	Class names: Use CamelCase.
•	Constants: Use ALL_CAPS_WITH_UNDERSCORES.
•	Avoid single-character variable names except for counters or simple variables like i, n, etc.'''

# 2. Indentation:
'''
•	Use 4 spaces per indentation level.
•	Avoid using tabs; only spaces should be used for indentation in Python.'''

# 3.	Whitespace in Expressions and Statements:
'''
•	Use spaces around operators 
e.g.

a + b rather than a+b

•	Avoid extra spaces inside parentheses, brackets, or braces.
e.g.'''

my_list = [1, 2, 3] # (Correct)
my_list = [ 1, 2, 3 ] # (Avoid extra spaces)

# 4. Blank Lines:
'''
•	Use two blank lines to separate top-level functions and class definitions.
e.g.'''

def function_one():
    pass


def function_two():
    pass


class MyClass:
    pass
'''
•	Use a single blank line to separate methods inside classes.
e.g.'''

class MyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass

# 5. Comments:
'''
•	Write comments that are clear and concise. They should explain why a piece of code exists, not how it works, which should 
    be clear from reading the code itself.
•	Use block comments for larger explanations.
•	Use inline comments sparingly for brief explanations next to specific lines.'''

# 6. Docstrings:
'''
•	Use docstrings to describe the purpose and usage of functions, classes, and modules.
•	Use triple double quotes (""") for all docstrings, whether they’re one-liners or multi-line descriptions, ensuring that 
    they’re compatible with Python’s help system and easy to identify.'''

# 7. Line Length:
'''
•	PEP8 suggests keeping lines under 79 characters for code and 72 characters for comments or docstrings. This makes code more 
    readable on various screen sizes and helps with side-by-side code comparisons.'''

# 8.	Organizing Imports:
'''
•	Group imports in this order:
i.	Standard library imports
ii.	Third-party imports
iii.Local application-specific imports
•	This helps clarify where each import comes from and improves code organization.
•	Avoid wildcard imports like from module import *; instead, explicitly list the specific functions or classes you need. 
    This maintains clarity on the origin of functions and classes, keeps dependencies clear, and prevents conflicts between 
    items with similar names.
•	Place Imports at the Top: Import statements should appear at the top of your file, under any module-level docstring or 
    comments, making dependencies immediately visible.'''

# 9. Other Conventions:
'''
•	Avoid Trailing Whitespace: Remove any extra spaces at the end of lines to keep the code clean and consistent.'''

# Why Follow PEP8?
'''
•	PEP8 is widely recognized in the Python community, so following it helps your code align with Python’s “readability counts” 
    philosophy, which is key to writing clear, maintainable code. 
•	This is especially helpful for teamwork, as it allows developers to quickly understand and contribute to each other’s 
    code in collaborative projects.'''
