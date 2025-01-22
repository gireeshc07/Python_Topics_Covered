
# List Comprehension in Python:
'''
-> List Comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
-> Instead of using a multi-line for loop to filter or transform data, you can achieve the same functionality with a single, compact line of code using list comprehension.
'''
# The Key Syntax: new_list = [expression for item in iterable if condition]
'''
-> Expression: The value or transformation applied to the current item.
-> Item: The current element being processed in the loop.
-> Iterable: Any iterable object (list, range, tuple, etc.).
-> Condition (Optional): A filter that decides whether to include the current item in the new list.
'''
# Components of List Comprehension:

# 1. Expression:
'''
-> The expression is the core of a list comprehension and determines what gets added to the new list. It is evaluated for each item in the iterable, and the result of this expression becomes an element in the final list.
-> Purpose: The expression can be as simple as directly using the item or as complex as applying functions, performing arithmetic, or transforming the data.
-> Characteristics:
    - Always evaluated for each item in the iterable.
    - The result of the evaluation is what gets appended to the list.
    - Can include functions, operations, method calls, or any valid Python expression.
'''
# e.g.,
# Simple transformation
numbers = [1, 2, 3, 4]
squares = [x**2 for x in numbers]  # Expression is x**2
print(squares)
# Output: [1, 4, 9, 16]

# Applying a function
words = ["apple", "banana", "cherry"]
uppercase_words = [word.upper() for word in words]  # Expression is word.upper()
print(uppercase_words)  
# Output: ['APPLE', 'BANANA', 'CHERRY']
'''
-> You can set the outcome to whatever you like.
'''
# e.g.,
newlist = ["hello" for x in words] # Replace all items
print(newlist)  
# Output: ['hello', 'hello', 'hello']
'''
-> The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
'''
# e.g.,
fruits=['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = [x if x != "banana" else "orange" for x in fruits] # Add conditional logic in the expression (If the item is "banana", replace it with "orange"; otherwise, keep the original value)
print(newlist) 
# Output: ['apple', 'orange', 'cherry', 'kiwi', 'mango']

# 2. Item:
'''
-> The item is the variable used to refer to each element of the iterable during the iteration process. It acts as a placeholder that holds the current element being processed.
-> Purpose: It allows you to reference and manipulate the current element within the expression or any part of the list comprehension.
-> Characteristics:
  - Defined within the list comprehension's syntax (typically before the for keyword).
  - Changes with each iteration as Python moves through the iterable.
  - Can be used as-is, transformed, or combined with other operations.
  - The name of the item variable is flexible but should be descriptive to enhance code readability.
'''
# e.g.,
# Using item directly
numbers = [1, 2, 3, 4]
doubled = [x * 2 for x in numbers]  # Item is x
print(doubled)  
# Output: [2, 4, 6, 8]

# Using item in a more complex expression
names = ["Alice", "Bob", "Charlie"]
name_lengths = [len(name) for name in names]  # Item is name
print(name_lengths)  
# Output: [5, 3, 7]

# 3. Iterable
'''
-> The iterable is the sequence or collection that provides the items to iterate over. It can be a list, tuple, set, dictionary, or even a generator.
-> Purpose: The iterable is what the list comprehension loops through, providing items for the item variable to process.
-> Characteristics:
  - Must be an object that implements Python’s iterator protocol (i.e., it has an __iter__() method).
  - Can be of any type, including built-in sequences (like lists and ranges) or custom iterables.
  - The iterable defines how many times the list comprehension loop runs and provides the data each time.
'''
# e.g.,
# Using a list as an iterable
nums = [10, 20, 30]
squared_nums = [num**2 for num in nums]  # Iterable is nums
print(squared_nums)  # Output: [100, 400, 900]

# Using a range as an iterable
even_numbers = [x for x in range(10) if x % 2 == 0]  # Iterable is range(10)
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

# 4. Condition
'''
-> The condition is an optional part of the list comprehension that filters which items are included in the final list. It acts as a filter, 
   evaluating to True or False for each item in the iterable.
-> Purpose: The condition allows you to selectively include items based on whether they meet certain criteria.
-> Characteristics:
  - The condition is placed after the for loop and is preceded by an if keyword.
  - Only items for which the condition evaluates to True are included in the resulting list.
  - Can be simple (e.g., checking divisibility) or complex (e.g., using logical operators).
'''
# e.g.,
# Example 1: Basic filtering
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]  # Condition: num % 2 == 0
print(even_numbers)  # Output: [2, 4, 6]

# Example 2: Condition with transformation
words = ["apple", "banana", "cherry"]
long_words = [word.upper() for word in words if len(word) > 5]  # Condition: len(word) > 5
print(long_words)  
# Output: ['BANANA', 'CHERRY']

# List comprehension with if-else:
'''
-> The list comprehensions can incorporate if-else conditions to create lists based on specific rules or transformations.
'''
# Syntax: [expression if condition else alternate_expression for item in iterable]
'''
-> expression_if_condition: Applied if the condition evaluates to True.
-> alternate_expression: Applied if the condition evaluates to False.
-> for item in iterable: Loops through each item in the iterable (like a list, range, etc.).
'''
# e.g.,
# 1. Categorize numbers into "Positive" and "Negative" based on their sign.
numbers = [-5, 3, 0, -1, 6]
categories = ["Positive" if num > 0 else "Negative or Zero" for num in numbers]
print(categories)
# Output: ['Negative or Zero', 'Positive', 'Negative or Zero', 'Negative or Zero', 'Positive']

# 2. Replace numbers greater than 5 with "High" and others with "Low".
values = [3, 7, 1, 9, 4]
labels = ["High" if value > 5 else "Low" for value in values]
print(labels)
# Output: ['Low', 'High', 'Low', 'High', 'Low']

# Combining All Components:
'''
-> A list comprehension can combine all four components to create powerful one-liners. Here's an example that uses all parts:
'''
# e.g.,
# Creating a list of squares of even numbers greater than 10
numbers = [5, 10, 15, 20, 25, 30]
squares_of_evens = [x**2 for x in numbers if x > 10 and x % 2 == 0]  # Expression, item, iterable, condition
print(squares_of_evens)
# Output: [400, 900, 1600, 900]

# Explanation:
'''
-> Expression: x**2 calculates the square of x.
-> Item: x represents the current number being processed from the numbers list.
-> Iterable: numbers is the list we are iterating over.
-> Condition: x > 10 and x % 2 == 0 ensures only even numbers greater than 10 are processed.
'''
# Advantages of List Comprehension

# 1. Conciseness: Reduces multi-line loops into a single line.
# 2. Readability: Clean and easier to understand for simple operations.
# 3. Efficiency: Faster than traditional loops due to Python optimizations.

# Use Cases of List Comprehension:

# 1. Transforming Data

# Convert all items to uppercase:
fruits = ["apple", "banana", "cherry"]
newlist = [x.upper() for x in fruits]
print(newlist)
# Output: ['APPLE', 'BANANA', 'CHERRY']

# Replace items conditionally:
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# Output: ['apple', 'orange', 'cherry']

# 2. Creating Lists

# Generate numbers using a range:
newlist = [x for x in range(10)]
print(newlist)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter numbers less than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)
# Output: [0, 1, 2, 3, 4]

# 3. Filtering Data

# Exclude a specific item:
newlist = [x for x in fruits if x != "apple"]
print(newlist)
# Output: ['banana', 'cherry']

# Extract even numbers:
numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  
# Output: [2, 4]

# 4. Nested Loops

# Generate pairs of numbers:
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  
# Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 5. Real-World Use Cases

# Flatten a nested list:
nested_list = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested_list for item in sublist]
print(flat)  
# Output: [1, 2, 3, 4, 5, 6]

# Extract specific data from dictionaries:
students = [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 40}]
high_scorers = [student["name"] for student in students if student["score"] > 50]
print(high_scorers)  
# Output: ['Alice']

# 6. Additional Use Cases

# Filter alphabets and digits from a string:
string = "Python 112233"
alphabets = [x for x in string if x.isalpha()]
digits = [x for x in string if x.isdigit()]
print(alphabets)  
# Output: ['P', 'y', 't', 'h', 'o', 'n']
print(digits)     
# Output: ['1', '1', '2', '2', '3', '3']

# Access nested list elements:
nested_list = [[1, 2, 3], [11, 23, 44]]
first_elements = [x[0] for x in nested_list]
print(first_elements)  
# Output: [1, 11]

# Generate data for analysis (Temperature conversion):
temperatures_in_celsius = [25, 30, 35, 40]
temperatures_in_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures_in_celsius]
print(temperatures_in_fahrenheit)  
# Output: [77.0, 86.0, 95.0, 104.0]

# 7. Function Calls

# Apply a function to list elements:
def square(x):
    return x * x

squares = [square(x) for x in range(1, 11)]
print(squares)  
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Complex Examples:

# 1. Nested Loops for Custom Combinations

# Sum combinations from two lists:
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = [x + y for x in list1 for y in list2]
print(sums)  
# Output: [11, 21, 31, 12, 22, 32, 13, 23, 33]

# 2. Conditional Expressions

# Modify numbers based on a condition:
numbers = [x if x > 4 else x + 1 for x in range(1, 11)]
print(numbers)  
# Output: [2, 3, 4, 5, 5, 6, 7, 8, 9, 10]

# 3. Filtering Numbers

# Even numbers divisible by 5:
numbers = [x for x in range(100) if x % 2 == 0 and x % 5 == 0]
print(numbers)  
# Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# 4. Extracting the data from a file

# Extracting lines containing the word "important":
with open("data.txt", "r") as file:
    important_lines = [line.strip() for line in file if "important" in line]
print(important_lines)
# Output: ['This is an important line of text.', 'This line is not so important.', 
#          'Another important insight is here.', 'Yet another important piece of information.']

# Limitations of List Comprehension:

# 1. Reduced Readability for Complex Logic: When dealing with multiple conditions or nested loops, list comprehensions can become hard to read and understand, reducing code clarity.
# 2. High Memory Usage for Large Data: List comprehensions generate the entire list in memory, making them inefficient for large datasets compared to generators.
# 3. Limited to Expressions, Not Statements: List comprehensions cannot directly include statements like print() or variable assignments, which limits their flexibility for complex operations.

# Examples:
# Case 1: Using print() in a list comprehension
'''
-> You may want to print each item while creating a list. However, print() doesn't produce a value that can be included in a list comprehension.
'''
# e.g.,
# Attempting to use print() in list comprehension
new_list = [print(x) for x in range(5)]
print(new_list)
# Output:
# 0
# 1
# 2
# 3
# 4
# [None, None, None, None, None]

# Explanation: The print() function returns None, so the resulting list is filled with None values. This is often not the intended behavior.

# Case 2: Performing Variable Assignments
'''
-> List comprehensions cannot include direct assignments to variables because assignments are statements, not expressions.
'''
# e.g.,
# Attempting to assign variables inside a list comprehension will raise a SyntaxError
# new_list = [x = x**2 for x in range(5)] # cannot use assignment expressions with list comprehensions
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

# Workaround for Variable Assignment:
'''
-> To perform assignments, you can use a regular loop or use assignment expressions (Walrus operator :=), but the latter may still reduce clarity:
'''
# e.g.,
# Using assignment expressions (Walrus operator)
new_list = [y := x**2 for x in range(5)]
print(new_list)  # Output: [0, 1, 4, 9, 16]
'''
-> However, this approach can still make the code harder to read compared to a traditional loop.
'''

# List Comprehension Use Cases:

# 1. Transforming Data

# Convert all items to uppercase:
fruits = ["apple", "banana", "cherry"]
newlist = [x.upper() for x in fruits]
print(newlist)
# Output: ['APPLE', 'BANANA', 'CHERRY']

# Replace items conditionally:
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# Output: ['apple', 'orange', 'cherry']

# 2. Creating Lists

# Generate numbers using a range:
newlist = [x for x in range(10)]
print(newlist)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter numbers less than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)
# Output: [0, 1, 2, 3, 4]

# 3. Filtering Data

# Exclude a specific item:
newlist = [x for x in fruits if x != "apple"]
print(newlist)
# Output: ['banana', 'cherry']

# Extract even numbers:
numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  
# Output: [2, 4]

# 4. Nested Loops

# Generate pairs of numbers:
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  
# Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 5. Real-World Use Cases

# Flatten a nested list:
nested_list = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested_list for item in sublist]
print(flat)  
# Output: [1, 2, 3, 4, 5, 6]

# Extract specific data from dictionaries:
students = [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 40}]
high_scorers = [student["name"] for student in students if student["score"] > 50]
print(high_scorers)  
# Output: ['Alice']

# 6. Additional Use Cases

# Filter alphabets and digits from a string:
string = "Python 112233"
alphabets = [x for x in string if x.isalpha()]
digits = [x for x in string if x.isdigit()]
print(alphabets)  
# Output: ['P', 'y', 't', 'h', 'o', 'n']
print(digits)     
# Output: ['1', '1', '2', '2', '3', '3']

# Access nested list elements:
nested_list = [[1, 2, 3], [11, 23, 44]]
first_elements = [x[0] for x in nested_list]
print(first_elements)  
# Output: [1, 11]

# Generate data for analysis (Temperature conversion):

temperatures_in_celsius = [25, 30, 35, 40]
temperatures_in_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures_in_celsius]
print(temperatures_in_fahrenheit)  
# Output: [77.0, 86.0, 95.0, 104.0]

# 7. Function Calls

# Apply a function to list elements:
def square(x):
    return x * x

squares = [square(x) for x in range(1, 11)]
print(squares)  
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Complex Examples:

# 1. Nested Loops for Custom Combinations

# Sum combinations from two lists:
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = [x + y for x in list1 for y in list2]
print(sums)  
# Output: [11, 21, 31, 12, 22, 32, 13, 23, 33]

# 2. Conditional Expressions

# Modify numbers based on a condition:
numbers = [x if x > 4 else x + 1 for x in range(1, 11)]
print(numbers)  
# Output: [2, 3, 4, 5, 5, 6, 7, 8, 9, 10]

# 3. Filtering Numbers

# Even numbers divisible by 5:
numbers = [x for x in range(100) if x % 2 == 0 and x % 5 == 0]
print(numbers)  
# Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# 4. Extracting the data from a file

# Extracting lines containing the word "important":
with open("data.txt", "r") as file:
    important_lines = [line.strip() for line in file if "important" in line]
print(important_lines)
# Output: ['This is an important line of text.', 
# 'This line is not so important.', 
# 'Another important insight is here.', 
# 'Yet another important piece of information.']

# Comparing List Comprehension to Traditional Loops:
'''
| Aspect            | List Comprehension                          | Traditional Loops                     |
|-------------------|---------------------------------------------|---------------------------------------|
|   Conciseness     | More concise and readable for simple tasks. | Requires more lines of code.          |
|   Readability     | Can be harder to read if too complex.       | Easier to follow for complex logic.   |
|   Performance     | Faster for small-to-medium tasks.           | Slightly slower due to explicit calls.|
|   Conditional     | Inline filtering and transformation.        | Requires separate `if` and `else`.    |'''
