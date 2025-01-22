"                                                                    🐍 Lists in Python 🐍                                                                                                         "

# Python Lists:
'''
-> Lists are used to store multiple values in a single variable.
-> List items are separated by comma(,) and enclosed by square brackets[].
-> Lists are ordered, changeable(mutable), indexed, allows duplicate values, and heterogeneous.
-> List has 11 built in methods.
'''
# Creating a list:

empty_list = []
print(empty_list)
# Output: []
print(type(empty_list))
# Output: <class 'list'>

empty_list = list()
print(empty_list)
# Output: []
print(type(empty_list))
# Output: <class 'list'>

my_list = [10, 20, 30, 40]
print(my_list)
# Output: [10, 20, 30, 40]

my_list = list((10, 20, 30, 40))
print(my_list)
# Output: [10, 20, 30, 40]

# List Indexing:

my_list = [10, 20, 30, 40]

# Access:
print(my_list[0])
# Output: 10

# Modify:
my_list[0] = 11
print(my_list)
# Output: [11, 20, 30, 40]

# Remove:
del my_list[0]
print(my_list)
# Output: [20, 30, 40]

del my_list
# print(my_list)
# Output: NameError: name 'my_list' is not defined. Did you mean: 'empty_list'?

# List Slicing:

my_list = [10, 20, 30, 40, 50, 60]

# Access:
print(my_list[0:4])
# Output: [10, 20, 30, 40] 

# Modify:
my_list[0:3] = [11, 22, 33]
print(my_list)
# Output: [11, 22, 33, 40, 50, 60]

# Remove:
del my_list[0:3]
print(my_list)
# Output: [40, 50, 60]

del my_list
# print(my_list)
# Output: NameError: name 'my_list' is not defined. Did you mean: 'empty_list'?

# Slice Method:

this_list = [10, 20, 30, 40, 50, 60]

# s = slice()
# print(this_list[s])
# Output: TypeError: slice expected at least 1 argument, got 0

s = slice(1, 5, 2)
print(s.start, s.stop, s.step)
# Output: 1 5 2

s = slice(0, 5, 2)
print(this_list[s])
# Output: [10, 30, 50]

# List Methods:
'''
-> It has 11 built in methods.
'''

# Method 1: insert()

my_list = [1, 2, 3, 4]
my_list.insert(2, 99)
print(my_list)
# Output: [1, 2, 99, 3, 4]

# Method 2: append()

my_list = [1, 2, 3, 4]
my_list.append(2)
print(my_list)
# Output: [1, 2, 3, 4, 2]

# Method 3: extend()

my_list = [1, 2, 3, 4]
my_list.extend([5, 6, 7])
print(my_list)
# Output: [1, 2, 3, 4, 5, 6, 7]

# Method 4: remove()

my_list = [1, 2, 3, 4, 2]
my_list.remove(2)
print(my_list)
# Output: [1, 3, 4, 2]

# Method 5: pop()

my_list = [1, 2, 3, 4]
my_list.pop(0)
print(my_list)
# Output: [2, 3, 4]

# Method 6: clear()

my_list = [1, 2, 3, 4]
my_list.clear()
print(my_list)
# Output: []

# Method 7: sort()

my_list = [1, 2, 3, 4, 5, 2]
my_list.sort()
print(my_list)
# Output: [1, 2, 2, 3, 4, 5]

my_list.sort(reverse=True)
print(my_list)
# Output: [5, 4, 3, 2, 2, 1]

# Method 8: reverse()

my_list = [1, 2, 3, 4, 5, 2]
my_list.reverse()
print(my_list)
# Output: [2, 5, 4, 3, 2, 1] 

# Method 9: copy()
'''
-> The copy() method is part of Python's built-in list methods. It creates a shallow copy of a list, meaning it duplicates the outer list but 
   does not create independent copies of any nested mutable objects (like sublists,dictionaries, etc.).'''

# Syntax: new_list = original_list.copy()
'''
-> The copy() method in Python does not take any arguments.
-> It does not return a value in the sense of a computed or modified result—it simply returns a new list (or object) that is a copy of the original.'''

# Shallow Copy:
'''
-> Only the outer list is duplicated.
-> If the list contains mutable objects (like sublists, dictionaries, or other custom objects), the new list will reference these objects instead 
   of creating new copies.
-> Any changes made to these nested objects will be reflected in both the original and the copied list.
'''
# 2. Independent Copy:
'''
-> The new list has a separate memory address, so modifying it won't affect the original list.'''

# Example 1: 

# Original list
original_list = [1, 2, 3]

# Create a shallow copy
copied_list = original_list.copy()

# Modify the copied list
copied_list[0] = 100

print("Original List:", original_list)  # Output: [1, 2, 3]
print("Copied List:", copied_list)      # Output: [100, 2, 3]

'''
The original list remains unaffected when you modify the copied list because the outer structure is independently copied.'''

# Example 2: 

original_list = [1, 2, [3, 4]]

# Create a shallow copy
copied_list = original_list.copy()

# Modify a nested list in the copied list
copied_list[2][0] = 100

print("Original List:", original_list)  # Output: [1, 2, [100, 4]]
print("Copied List:", copied_list)      # Output: [1, 2, [100, 4]]
'''
-> Both lists are affected because the `copy()` method does not duplicate the nested list. Instead, both the original and copied lists share the 
   same reference to the nested list [3, 4].'''

# Alternatives:
'''
-> For a  deep copy  (to recursively copy nested objects), use the copy module.'''

# Deep Copy (copy.deepcopy()):
'''
-> Recursively duplicates all objects in the list, including nested structures.
-> Changes made to nested objects in the copied list will not affect the original list.'''

# Example:

import copy

original_list = [1, 2, [3, 4]]

# Create a deep copy
deep_copied_list = copy.deepcopy(original_list)

# Modify the nested list in the deep copy
deep_copied_list[2][0] = 100

print("Original List:", original_list)      # Output: [1, 2, [3, 4]]
print("Deep Copied List:", deep_copied_list)  # Output: [1, 2, [100, 4]]
'''
-> Changes to the deep copy do not affect the original list because `deepcopy()` creates an entirely new structure, including for nested elements.'''

# Why Use copy()?

# 1. Avoids modifying the original list:  
'''
- If you want to work on a separate copy without affecting the original list, copy() is a convenient way to achieve that. However, it is only 
  suitable for flat lists and not for lists containing nested mutable objects. For complete independence from the original list, use deepcopy().'''

# 2. Improves readability and intent: 
'''
-> Instead of using slicing (new_list = original_list[:]), copy() explicitly shows your intention to create a duplicate, improving code readability.'''

# Different ways to copy a list:

# 1. copy() Method:

# Example:

# Using copy() with a list
original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)  # Output: [1, 2, 3]

# Using copy() with a tuple
original_tuple = (1, 2, 3)
# copied_tuple = original_tuple.copy()  # AttributeError: 'tuple' object has no attribute 'copy'

# Using copy() with a set
original_set = {1, 2, 3}
copied_set = original_set.copy()
print(copied_set)  # Output: {1, 2, 3}

# 2. Slicing ([:]):

# Example:

# Using slicing with a list
original_list = [1, 2, 3]
copied_list = original_list[:]
print(copied_list)  # Output: [1, 2, 3]

# Using slicing with a tuple
original_tuple = (1, 2, 3)
copied_tuple = original_tuple[:]
print(copied_tuple)  # Output: (1, 2, 3)

# Using slicing with a string
original_string = "hello"
copied_string = original_string[:]
print(copied_string)  # Output: "hello"

# 3. list() Constructor:

# Example:

# Using list() with a range
range_obj = range(5)
copied_list = list(range_obj)
print(copied_list)  # Output: [0, 1, 2, 3, 4]

# Using list() with a set
original_set = {1, 2, 3}
copied_list = list(original_set)
print(copied_list)  # Output: [1, 2, 3] (order may vary)

# Using list() with a generator
generator = (x**2 for x in range(3))
print(type(generator)) # Output: <class 'generator'>
print(generator) # Output: <generator object <genexpr> at 0x000001DDDA8C36B0>

copied_list = list(generator)
print(copied_list)  # Output: [0, 1, 4]

# Method 10. copy()

# Syntax: list.count(element)

'''
-> The count() method in Python is used to determine how many times a specific element appears in a list, tuple, or string.
-> It takes one argument, which is the item you want to count in the list.'''

# Key Points:

# 1. The method does not modify the original list; it only returns the count.

# e.g.

my_list = [1, 2, 3, 4, 2, 2]
count_of_2 = my_list.count(2)
print(count_of_2)  # Output: 3

# 2. The count() method is case-sensitive for strings.

# e.g.

words = ["Python", "python", "PYTHON"]
# print(words.count("python"))  # Output: 1

# 3. If the element is not found, the method returns 0.

# e.g.

animals = ["cat", "dog", "bird"]
count_lion = animals.count("lion")
# print(count_lion)  # Output: 0

# 4. If nothing is specified, it raises a TypeError.

# e.g.

numbers = [1, 2, 3, 4, 2, 2]
# count = numbers.count()
# Output: TypeError: list.count() takes exactly one argument (0 given)

# Use Case
'''
-> The count() method is useful when you need to find out how many times an item appears in a list, such as counting occurrences of a certain item 
   in a survey, finding duplicates, or analyzing the frequency of elements.'''

# Behavior of the count() Method with Different Data Types:
'''
-> count() works with lists, strings, and tuples. It does not work with non-sequence types like dictionaries or sets.'''

# Why count() Works with Lists, Strings, and Tuples:
'''
-> These are sequence types, meaning they have ordered elements that can be iterated. count() iterates over the sequence to count occurrences of a 
   specific element.'''

# Why count() Does Not Work with Dictionaries or Sets:
'''
-> Dictionaries: They are key-value pairs, not sequences. Although you can iterate through their keys, values, or items, count() is not supported 
                 because dictionaries do not maintain a positional order.
-> Sets: These are unordered collections of unique elements. Since there are no duplicates, counting occurrences is unnecessary.'''

# Examples:

# count() in Lists:
my_list = [1, 2, 3, 1, 2, 1]
print(my_list.count(1))  # Output: 3

# count() in Strings:
my_string = "hello world"
print(my_string.count("o"))  # Output: 2

# count() in Tuples:
my_tuple = (1, 2, 3, 1, 1)
print(my_tuple.count(1))  # Output: 3

# count() in Dictionaries:
my_dict = {"a": 1, "b": 2}
# print(my_dict.count(1))  # AttributeError: 'dict' object has no attribute 'count'

# count() in Sets:
my_set = {1, 2, 3}
# print(my_set.count(1))  # AttributeError: 'set' object has no attribute 'count'

'''
-> The count() method works with any data type present in a list, such as numbers, strings, booleans, and even nested lists, dictionaries, and 
   sets. However, it’s important to understand how count() operates with different types and structures.'''

# Works with Numbers, Strings, and Booleans
'''
-> The count() method can count occurrences of numbers, strings, and booleans in a list. These types are straightforward because they are hashable 
   and their equality checks are simple.'''
   
# Examples:

numbers = [1, 2, 3, 2, 1, 1]
print(numbers.count(1))  # Output: 3

strings = ["apple", "banana", "apple", "cherry"]
print(strings.count("apple"))  # Output: 2

booleans = [True, False, True, True, False]
print(booleans.count(True))  # Output: 3

# Handles Nested Lists
'''
-> The method can count occurrences of nested lists as long as they match exactly in structure and content.'''

# Examples:

nested_lists = [[1, 2], [3, 4], [1, 2]]
print(nested_lists.count([1, 2]))  # Output: 2

# Handles Dictionaries and Sets in a List
'''
-> The count() method can count dictionaries and sets inside a list if they match exactly in structure and content.

Dictionaries: The keys and values must match exactly.
Sets: The elements must match, though order does not matter due to the unordered nature of sets.'''

# Examples:

nested_dicts = [{"a": 1}, {"b": 2}, {"a": 1}]
print(nested_dicts.count({"a": 1}))  # Output: 2

nested_sets = [{1, 2, 3}, {3, 2, 1}, {4, 5}]
print(nested_sets.count({1, 2, 3}))  # Output: 2

# Important Considerations:

# Exact Match:
'''
-> count() requires an exact match. The type, structure, and values must be identical for the method to count an element.'''

# Unhashable Elements in Sets and Dictionaries:
'''
-> Elements like lists, which are unhashable, cannot be included in sets or as dictionary keys. Attempting to do so raises a TypeError. 
-> This limitation does not affect the count() method itself but is a constraint of Python's data structures.'''

# Example

# invalid_set = [{1, 2, 3}, {4, [5, 6]}]  # Raises a TypeError because [5, 6] is unhashable.

# Conclusion:
'''
-> The count() method is versatile and works with various data types in lists and tuples, including nested structures like lists, dictionaries, 
   and sets. 
-> However, it is essential to remember that count() performs an exact match, so the item being counted must match in value and type. 
-> This method does not work with unhashable types inside sets or dictionaries, ensuring data integrity in your operations.'''

# Method 11: index()
'''
-> It returns the index (position) of the first occurrence of a specified element in the list. 
-> If the element is not found, it raises a ValueError.
-> The index() method is available for all sequence types.
'''
# Syntax : list.index(element, start, end)
'''
-> element: The item you want to find in the list.
-> start (optional): The starting position in the list where the search begins.
-> end (optional): The ending position in the list where the search stops.'''

# Examples

# Basic Usage
fruits = ["apple", "banana", "cherry", "apple"]
print(fruits.index("apple"))  # Output: 0 (first occurrence of "apple")

# With start Parameter
fruits = ["apple", "banana", "cherry", "apple"]
print(fruits.index("apple", 1))  # Output: 3 (search starts at index 1)

# With start and end Parameters
numbers = [1, 2, 3, 4, 2, 5]
print(numbers.index(2, 2, 5))  # Output: 4 (searches between indices 2 and 5)

# Element Not Found
colors = ["red", "blue", "green"]
# print(colors.index("yellow"))  # Raises ValueError: 'yellow' is not in list

# To avoid ValueError, you can check if an element exists in the list using in before calling index():
if "yellow" in colors:
   print(colors.index("yellow"))
else:
   print("Element not found")
   
# Common Use Cases
'''
-> Locating the position of an element in a list.
-> Identifying duplicates by combining with a loop.
-> Debugging to check the location of specific elements.'''
'''
To find all the index numbers of a specific element in a list, you can use a loop or list comprehension along with the enumerate() function. 
Here's how you can do it:'''

# Example 1: Using a Loop with the enumerate() function

# List to search
items = ["apple", "banana", "apple", "cherry", "apple"]

# Element to find
target = "apple"

# Initialize an empty list to store indices
indices = []

# Use a for loop with enumerate to iterate through the list
for i, value in enumerate(items):
    if value == target:
        indices.append(i)

print(indices)  # Output: [0, 2, 4]

# Explanation
'''
1. enumerate():
   - Provides both the index (i) and the value (value) for each element in the list.
2. if value == target:
   - Checks if the current value matches the target element.
3. indices.append(i):
   - Adds the index (i) to the list indices whenever the condition is true.'''

# Example 2: Using a List Comprehension with the enumerate() function

# List to search
items = ["apple", "banana", "apple", "cherry", "apple"]

# Element to find
target = "apple"

# Finding all indices using a list comprehension
indices = [i for i, value in enumerate(items) if value == target]
print(indices)  # Output: [0, 2, 4]

# Example 3: Custom Function for Reusability
'''
You can create a function to find all indices of a given element:'''

def find_all_indices(list, element):
    return [i for i, value in enumerate(list) if value == element]

# Example usage
items = ["apple", "banana", "apple", "cherry", "apple"]
print(find_all_indices(items, "apple"))  # Output: [0, 2, 4]
print(find_all_indices(items, "banana"))  # Output: [1]
print(find_all_indices(items, "orange"))  # Output: []

# Example 4: Using a loop Without the enumerate() function

# List to search
items = ["apple", "banana", "apple", "cherry", "apple"]

# Element to find
target = "apple"

# Initialize an empty list to store indices
indices = []

# Use a for loop with range() to iterate through indices
for i in range(len(items)):
    if items[i] == target:
        indices.append(i)

print(indices)  # Output: [0, 2, 4]

# 1. List Concatenation
'''
-> Joining two or more lists into a single list by combining their elements.
-> Addition(+) operator is used.
-> It does not modify the original list; instead, it creates a new one'''

# Example:

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# Concatenation Use Cases:

# 1. Merging Data: Combine multiple datasets stored in lists.

sales_2023 = [100, 200, 300]
sales_2024 = [400, 500, 600]
combined_sales = sales_2023 + sales_2024
print(combined_sales)  # Output: [100, 200, 300, 400, 500, 600]

# 2. Dynamic Content: Add additional elements to an existing list dynamically.

menu = ["Pizza", "Burger"]
specials = ["Pasta"]
updated_menu = menu + specials
print(updated_menu)  # Output: ['Pizza', 'Burger', 'Pasta']

# 2. List Repetition
'''
-> Creating a new list by repeating the elements of an existing list a specified number of times.
-> Multiplication(*) operator is used.
-> It does not modify the original list; instead, it creates a new one.
-> The repetition count must be a non-negative integer. If it’s 0 or negative integer, the result is an empty list.'''

# Example:

list1 = [1, 2, 3]
result = list1 * 3
print(result)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

list1 = [1, 2, 3]
result = list1 * 0
print(result)  # Output: []

list1 = [1, 2, 3]
result = list1 * -1
print(result)  # Output: []

# Repetition Use Cases:

# 1. Pattern Creation: Create repeated sequences for testing or simulations.

pattern = [1, 0] * 5
print(pattern) # Output: [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# 2. Placeholder Initialization: Initialize a list with repeated default values.

zeros = [0] * 10
print(zeros) # Output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Combining Both Operations
'''
-> You can use concatenation and repetition together to create complex patterns in lists.'''

# Example:

list1 = [1, 2, 3]
list2 = [4, 5]
result = (list1 * 2) + list2
print(result)  # Output: [1, 2, 3, 1, 2, 3, 4, 5]

# Differences Between Concatenation and Repetition
'''
|   Aspect                 |   Concatenation (+)                    |   Repetition (*)                     |
|--------------------------|----------------------------------------|--------------------------------------|
|   Purpose                | Combines multiple lists                | Repeats elements in a single list    |
|   Input                  | Two or more lists                      | One list and a repetition count      |
|   Output                 | A new list with combined elements      | A new list with repeated elements    |
|   Original Lists         | Remain unchanged                       | Remain unchanged                     |
|   Operator               | '+'                                    | '*'                                  |
|   Example                | [1, 2] + [3, 4] -> [1, 2, 3, 4]        | [1, 2] * 3 -> [1, 2, 1, 2, 1, 2]     |

-> By mastering list concatenation and repetition, you can handle a variety of scenarios in Python programming, from data 
   manipulation to generating patterns.'''

# Joining Two Lists:

"In Python, you can join two lists using several methods. Here's a detailed explanation with examples:"

# 1. Using + Operator
'''
-> The + operator concatenates two lists to create a new list. It does not modify the original list.'''

# Example:

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# 2. Using extend() Method
'''
-> The extend() method adds elements of another list to the end of the first list. It modifies the original list.'''

# Example:

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

# 3. Using List Comprehension
'''
-> List comprehension can be used to combine two lists into a new list.'''

# Example:

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = [item for item in list1] + [item for item in list2]
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# 4. Using * (Unpacking Operator)
'''
-> The unpacking operator  can be used to combine lists into a new list.'''

# Example:

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Join using unpacking
result = [*list1, *list2]

print(result)  # Output: [1, 2, 3, 4, 5, 6]

# 5. Using chain() from itertools
'''
-> The chain() function from the itertools module combines multiple lists efficiently, especially for larger lists.'''

# Example:

import itertools

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Join using itertools.chain
result = list(itertools.chain(list1, list2))

print(result)  # Output: [1, 2, 3, 4, 5, 6]

# 6. Using a for Loop
'''
-> You can iterate through the elements of the second list and append them to the first list.'''

# Example:

list1 = [1, 2, 3]
list2 = [4, 5, 6]
for item in list2:
    list1.append(item)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

# Which Method to Use?
'''
+ Operator         : You want a quick and simple way to join two lists into a new list.
* Operator         : You want to unpack multiple lists into a new list in a Pythonic way.
extend()           : You want to modify an existing list by appending elements from another list.
List Comprehension : You want to customize how the elements are joined (e.g., applying transformations or filters).
chain()            : You are dealing with a large number of lists or need to iterate over the combined elements without creating
                     a new list in memory.
Loop               : You want fine-grained control over how elements are added or need to process elements during joining.'''

# Loop Through a List:
# 1. for loop:
# e.g.

my_list=["apple","banana","cherry"]
for x in my_list:
   print(x,end=" ")
# Output: apple banana cherry

print()
my_list=["apple","banana","cherry"]
for i in range(len(my_list)):
   print(my_list[i],end=" ")
# Output: apple banana cherry

# 2. while loop:
# e.g.

print()
my_list=["apple","banana","cherry"]
i=0
while i<len(my_list):
   print(my_list[i],end=" ")
   i=i+1
# Output: apple banana cherry
