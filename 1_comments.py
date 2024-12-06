
# Python Comments:
"""
-> In Python, comments are lines that are ignored by the interpreter during the execution of the program. 
-> They are essential for improving code readability and maintaining clean, understandable code.
"""
# Why Use Comments?
"""
-> Explain Python code.
-> Make the code more readable.
-> Disable parts of code during testing.
-> Understand code later when revisiting after a long time."""

# Types of Comments in Python:

# 1. Single-Line Comments:
"""
-> Starts with # and continues until the end of the line.
-> If the comment needs to span multiple lines, each line must start with a #.
-> Best used for quick notes about variables, functions, or code behavior.

e.g."""

# This is a single-line comment

# 2. Multi-Line Comments:
"""
-> Python does not have a specific syntax for multi-line comments, but we can create them in two ways:"""

# Option 1: Multiple # hashtags
"""
-> We can multiple hashtags (#) to write multiline comments in Python but each and every line will be considered as a single-line comment.

e.g."""

# This is a multi-line comment
# written across several lines
# using individual hashtags.

# Option 2: String Literals (Docstrings)
"""
-> String literals can act as comments if they are not assigned to a variable.
-> Can be used for both single-line or multi-line comments.

e.g."""

"""
This is a multi-line comment
using a string literal.
It spans multiple lines.
"""

# What is a String Literal?
"""
-> A string literal is a sequence of characters enclosed within single quotes('') or double quotes("").
-> It is used to represent text data and can include letters, numbers, symbols, or whitespace.
"""

# Why Use String Literals for Comments?
"""
-> If not assigned to a variable, Python ignores them during execution.
-> You can use them as single-line or multi-line comments in place of hashtags.

e.g."""

"This is a single-line comment using a string literal"
'''
This is a multi-line comment
written using triple quotes.
'''

# Inline comments:
"""
-> Comments can be placed at the end of a line, and Python will ignore the rest of the line. These are called inline comments.

Important Note: For inline comments, always use hashtag(#) since string literals won't work in this context.

e.g."""

print("Hello, World!")  # Inline comment explaining the print function