"                                                                      🐍 Tuples in Python 🐍                                                                                                    "

# Python Tuples:
'''
-> In Python, a tuple is an immutable, ordered collection of elements.
-> Tuples are similar to lists, but their immutability makes them unique and useful for specific use cases where the data should not be changed.
-> Tuples are used to store multiple items in a single variable.
-> Tuples are written with round brackets () and their items are separated by commas.
-> Built-in Methods: Tuples have only two built-in methods:
   1. count(): Returns the number of times a specified value occurs in the tuple.
   2. index(): Returns the index of the first occurrence of a specified value in the tuple.
'''
# Characteristics of Tuples:
'''
1. Ordered: Elements in a tuple have a defined order, and that order will not change.
2. Unchangeable(Immutable): Once a tuple is created, its contents cannot be altered (no adding, removing, or modifying elements).
3. Indexed : Indexed - first item has index 0, second item has index 1
4. Allow Duplicates: Since tuples are indexed, they can have items with the same value.
5. Heterogeneous: Tuples can store elements of different data types (e.g., integers, strings, objects).
6. Hashable: Tuples are hashable by default if all their elements are hashable. However, if a tuple contains mutable or unhashable objects (like lists or dictionaries), it becomes unhashable.            
'''
# 1. Creating Tuples:

# Using Parentheses
my_tuple = (1, 2, 3)
print(my_tuple)  
# Output: (1, 2, 3)
print(type(my_tuple))
# Output: <class 'tuple'>

# Using the tuple() Constructor
list_to_tuple = tuple([1, 2, 3])
print(list_to_tuple)  
# Output: (1, 2, 3)
print(type(list_to_tuple))
# Output: <class 'tuple'>

# Empty Tuple:
empty_tuple = ()
print(empty_tuple)  
# Output: ()
print(type(empty_tuple))
# Output: <class 'tuple'>
'''
-> We can create a tuple with only one item, to do that we have to add a comma after the item, otherwise Python will not recongnize it as a tuple.
'''
# e.g.,

single_element = (5,)
print(single_element)
# Output: (5,)
print(type(single_element))  
# Output: <class 'tuple'>

my_tuple=1,
print(my_tuple)
# Output: (1,)
print(type(my_tuple))
# Output: <class 'tuple'>

my_tuple=1,2,3,4
print(my_tuple)
# Output: (1, 2, 3, 4)
print(type(my_tuple))
# Output: <class 'tuple'>

string=("abc")
print(string)
# Output: abc
print(type(string))
# Output: <class 'str'>

integer=(20)
print(integer)
# Output: 20
print(type(integer))
# Output: <class 'int'>

my_list=([1])
print(my_list)
# Output: [1]
print(type(my_list))
# Output: <class 'list'>

# 2. Accessing Tuples

my_tuple = (10, 20, 30, 40)

print(my_tuple[0])  
# Output: 10
print(my_tuple[-1]) 
# Output: 40

print(my_tuple[1:3])  
# Output: (20, 30)
print(my_tuple[-1:-3:-1])
# Output: (40, 30)
print(my_tuple[-3:-1])
# Output: (20, 30)

# Nesting Tuples
nested_tuple = (1, (2, 3), (4, (5, 6)))
print(nested_tuple[1][1])  
# Output: 3
print(nested_tuple[2][1]) 
# Output: (5, 6)
print(nested_tuple[2][1][0]) 
# Output: 5

# 3. Modifying Tuples:

my_tuple=(1,2,3,4)
# my_tuple[0]=10
# Output: TypeError: 'tuple' object does not support item assignment

my_tuple=(1,2,3,4)
my_list = list(my_tuple)
my_list[0]=10
my_tuple=tuple(my_list)
print(my_tuple)
# Output: (10, 2, 3, 4)

my_tuple=(1,2,3,4)
my_list = list(my_tuple)
my_list.append(10)
my_tuple=tuple(my_list)
print(my_tuple)
# Output: (1, 2, 3, 4, 10)

my_tuple1=(1,2,3,4)
my_tuple2=(10,)
my_tuple1+=my_tuple2
print(my_tuple1)
# Output: (1, 2, 3, 4, 10)

# Although tuples are immutable, if they contain mutable elements (like lists), those elements can be changed.
my_tuple = (1, [2, 3], 4)
my_tuple[1][0] = 99
print(my_tuple)
# Output: (1, [99, 3], 4)

# 4. Removing Tuples:
my_tuple=(1,2,3,4)
# del my_tuple[0]
# Output: TypeError: 'tuple' object doesn't support item deletion

my_tuple=(1,2,3,4)
my_list = list(my_tuple)
my_list.remove(1)
my_tuple=tuple(my_list)
print(my_tuple)
# Output: (2, 3, 4)

my_tuple=(1,2,3,4)
del my_tuple
# print(my_tuple)
# Output: NameError: name 'my_tuple' is not defined.

# 5. Tuple Methods
'''
-> Tuples have limited built-in methods due to their immutability:

1. tuple.count(element)

-> element: The value you want to count in the tuple.

-> Return Value: The method returns an integer representing the number of times the specified element appears in the tuple.

2. tuple.index(element, start, end)

-> element: The value for which the index is being searched.
-> start (optional): The starting position to search (default is the beginning of the tuple).
-> end (optional): The ending position to search (default is the end of the tuple).

-> Return Value: The method returns the index of the first occurrence of the specified element. If the element is not found, it raises a ValueError.
'''
# e.g.,

my_tuple = (1, 2, 2, 3)
print(my_tuple.count(2))  
# Output: 2
my_tuple = ("Python", "python", "PYTHON") # Case-Sensitive for Strings
print(my_tuple.count("python"))  
# Output: 1

my_tuple = (1, 2, 2, 3)
print(my_tuple.index(2))  
# Output: 1
print(my_tuple.index(2,2)) 
# Output: 2

my_tuple = ("Python", "python") # Case-Sensitive for Strings
print(my_tuple.index("python"))  
# Output: 1
print(my_tuple.index("HTML"))
# Output: ValueError: tuple.index(x): x not in tuple

# 6. Tuple Operations

# Concatenation: Combine tuples using the + operator.
tuple1 = (1, 2)
tuple2 = (3, 4)
print(tuple1 + tuple2)  
# Output: (1, 2, 3, 4)

# Repetition: Repeat tuples using the * operator.
print(tuple1 * 2)  
# Output: (1, 2, 1, 2)

# Membership Testing: Use in and not in to check for element existence.
print(2 in tuple1)  
# Output: True

# Length: Find the number of elements in a tuple.
print(len(tuple1))  
# Output: 2

# 7. Unpacking a Tuple

fruits = ("apple", "banana", "cherry")
print(fruits)
# Output: ('apple', 'banana', 'cherry')

a,b,c = fruits
print(a,b,c)
# Output: apple banana cherry

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
a,b,*c = fruits
print(a,b,c)
# Output: apple banana ['cherry', 'strawberry', 'raspberry']

a,*b,c = fruits
print(a,b,c)
# Output: apple ['banana', 'cherry', 'strawberry'] raspberry

a,b,*c = ("apple", "banana")
print(a,b,c)
# Output: apple banana []

a,b,c,*d = ("apple", "banana")
# Output: ValueError: not enough values to unpack (expected at least 3, got 2)

# 8. Loop through tuple elements:

my_tuple= (1,2,3)
for value in my_tuple:
    print(value)
# Output: 1
#         2
#         3

for i in range(len(my_tuple)):
    print(my_tuple[i])
# Output: 1
#         2
#         3

i=0
while i<len(my_tuple):
    print(my_tuple[i])
    i+=1
# Output: 1
#         2
#         3

# 9. Applications of Tuples:

# Fixed Data: Use tuples for data that should not change (e.g., coordinates, days of the week)
coordinates = (10, 20)
print(coordinates)  
# Output: (10, 20)

# Tuples can be used as dictionary keys because they are hashable
my_dict = {(10, 20): "point1", (30, 40): "point2"}
print(my_dict[(10, 20)])  
# Output: point1

# Elements in Sets
my_set = {(10, 20), (30, 40)}
print((10, 20) in my_set)  
# Output: True

# Functions can return multiple values as tuples
def get_stats():
    return 10, 20

stats = get_stats()
print(stats)  
# Output: (10, 20)

# 10. Advanced Concepts:

# Named Tuples: Use collections.namedtuple for tuples with named fields.

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)  
# Output: 10 20

# Summary
'''
-> Tuples are immutable, ordered collections used for fixed data or data that should not change.
-> They provide efficient storage, hashability, and versatility in Python programming.
-> Understanding tuples is crucial for working with Python's data structures and returning multiple values in functions.
'''

# 1. Hashable tuple:

t1 = (1, 2, 3)
print(hash(t1))  
# Output: A hash value (integer)

t2 = ((1, 2), (3, 4))
print(hash(t2))  
# Output: A hash value (integer)

# 2. Unhashable tuple:

# Tuple with an unhashable element (list)
t3 = (1, [2, 3])  # A list is not hashable
# print(hash(t3))  
# # TypeError: unhashable type: 'list'

# Tuple with an unhashable element (dictionary)
t4 = (1, {'key': 'value'})  # A dictionary is not hashable
# print(hash(t4))  
# # TypeError: unhashable type: 'dict'
