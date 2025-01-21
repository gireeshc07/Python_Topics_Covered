"                                                              🐍 Sets in Python 🐍                                                                                                             "

# Python Sets
'''
-> In Python, a set is an unordered and mutable collection of unique elements that does not allow duplicates.
-> Sets are used to store multiple items in a single variable.
-> Set items are enclosed by curly brackets and separated by commas.
-> They are great for membership testing and performing mathematical set operations such as union, intersection, and difference.
-> Use frozenset if an immutable set is required.
-> It has 17 built in methods.
'''
# Key Characteristics of Sets
'''
1. Unordered: do not have a defined order, so you can't be sure in which order the items will appear
2. mutable: Sets themselves can be modified (elements can be added or removed), but the elements within a set must be immutable (e.g., numbers, strings, or tuples).
3. Unindexed: do not have index numbers, so we can't access, modify, or remove using index numbers.
4. No duplicate values: do not allow more than one item with the same value.
5. Unique Elements: A set automatically removes duplicate elements.
6. Heterogeneous: A set can store a mix of integers, strings, floats, tuples, and other hashable types, as long as all elements are immutable and hashable.
7. Unhashable: Since sets can have their elements added or removed after creation, they cannot provide a consistent hash valueand are therefore unhashable. If you try to use a set as a key in a dictionary or as an element in another set, you will encounter a TypeError.
8. Dynamic: Sets are dynamic and can grow or shrink as elements are added or removed.
'''
# Creating Sets:

# Using Curly Braces:
my_set = {1, 2, 3}
print(my_set)
# Output: {1, 2, 3}
print(type(my_set))
# Output: <class 'set'>

# Using the set() Constructor:
my_set = set([1, 2, 3])  # From a list
print(my_set)
# Output: {1, 2, 3}
print(type(my_set))
# Output: <class 'set'>

# Converts a string into a set of unique characters
my_set = set("hello")
print(my_set)
# Output: {'h', 'e', 'l', 'o'}
print(type(my_set))
# Output: <class 'set'>

# Creating an empty set
empty_set = set()
print(empty_set)
# Output: set()
print(type(empty_set))
# Output: <class 'set'>

empty_dict = {}
print(empty_dict)
# Output: {}
print(type(empty_dict))
# Output: <class 'dict'>

my_set = {1,2,2,3,3,4,4,5,5,6,6}
print(my_set)
# Output: {1, 2, 3, 4, 5, 6}

my_set = {"apple","banana","cherry",True,1,2}
print(my_set)
# Output: {True, 2, 'apple', 'cherry', 'banana'}

my_set = {"apple","banana","cherry",False,0,2}
print(my_set)
# Output: {False, 2, 'apple', 'cherry', 'banana'}

my_set = {1, 2, 3}
# my_set[0] = 10
# Output: TypeError: 'set' object does not support item assignment

# Set Methods:

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
# Output: {1, 2, 3, 4}

my_set = {1, 2, 3}
my_set.update([4,5,6])
print(my_set)
# Output: {1, 2, 3, 4, 5, 6}

my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set)
# Output: {1, 2, 4}

my_set = {1, 2, 3, 4}
my_set.discard(3)
print(my_set)
# Output: {1, 2, 4}

my_set = {1, 2, 3, 4}
my_set.pop()
print(my_set)
# Output: {2, 3, 4}

my_set = {1, 2, 3, 4}
my_set.clear()
print(my_set)
# Output: set()

original_set = {1, 2, 3, 4}
copied_set = original_set.copy()
print(copied_set)
# Output: {1, 2, 3, 4}

# Mathematical Set Operation: 

# Union (| or union())
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
print(fs1 | fs2)  
# Output: frozenset({1, 2, 3, 4, 5})

# Intersection (& or intersection())
print(fs1 & fs2)  
# Output: frozenset({3})

# Difference (- or difference())
print(fs1 - fs2)  
# Output: frozenset({1, 2})

# Symmetric Difference (^ or symmetric_difference())
print(fs1 ^ fs2)  
# Output: frozenset({1, 2, 4, 5})

# Membership Testing:
'''
-> You can check if an element exists in a set using the in keyword.
'''
# e.g.,

my_set = {1, 2, 3}
print(2 in my_set)  
# Output: True
print(4 in my_set)  
# Output: False

# Set Comprehensions:
'''
-> Set comprehensions are similar to list comprehensions, but they create a set.
'''
# e.g.,

squared_set = {x**2 for x in range(5)}
print(squared_set)  
# Output: {0, 1, 4, 9, 16}

# Methods to Access Set Items:
'''
-> In Python, sets are unordered collections of unique elements, so there is no concept of indexing or direct access by position as in lists or tuples. 
-> However, you can access items in a set indirectly using iteration or by converting the set to a list or tuple.
'''
# e.g.,

# Iterating Through the Set
my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)
# Output:
# apple
# banana
# cherry

# Using the in Keyword
my_set = {"apple", "banana", "cherry"}
if "banana" in my_set:
    print("Banana is in the set!")
# Output: Banana is in the set!

# Converting Set to a List or Tuple
my_set = {"apple", "banana", "cherry"}
my_list = list(my_set)  # Convert to list
print(my_list[0])       # Access first item
# Output: (order may vary due to the unordered nature of sets): apple

# Using the next() Function
my_set = {"apple", "banana", "cherry"}
iterator = iter(my_set)
print(next(iterator))  # Get the first item
# Output: apple

# Frozen Sets:
'''
-> A frozen set is an immutable version of a set. Once created, elements cannot be added or removed.
-> Frozensets are useful when you need a hashable collection of unique items, such as keys in a dictionary or elements in another set.
'''

# Key Characteristics of Frozensets:
'''
1. Immutable: Once created, a frozenset cannot be modified.
2. Hashable: Unlike regular sets, frozensets are hashable, so they can be used as keys in dictionaries or elements in other sets.
3. Unordered: Like sets, frozensets do not maintain any specific order of their elements.
4. Unique Elements: Duplicate elements are automatically removed when creating a frozenset.
'''

# Creating a Frozenset:
'''
-> To create a frozenset, use the frozenset() constructor. You can pass any iterable to it (e.g., lists, tuples, or strings).
'''
# e.g.,

# Creating a frozenset
fs = frozenset([1, 2, 3, 2])  # Duplicates are removed
print(fs)
# Output: frozenset({1, 2, 3})
print(type(fs))
# Output: <class 'frozenset'>

# From a string
fs = frozenset("hello")
print(fs)
# Output: frozenset({'h', 'e', 'l', 'o'})

# fs[0] = "b"
# Output: TypeError: 'frozenset' object does not support item assignment

ls = list(fs)
ls[0] = "b"
fs = frozenset(ls)
print(fs)
# Output: frozenset({'o', 'b', 'l', 'h'})

# Frozenset Operations:
'''
-> Frozensets support all set operations, but since they are immutable, methods like add(), remove(), or clear() are not available.
-> Instead, you can perform mathematical set operations and other read-only operations.
'''

# Methods available for frozensets:
'''
1. copy()	                         
2. union(iterable)	                 
3. intersection(iterable)	         
4. difference(iterable)	         
5. symmetric_difference(iterable) 	 
6. isdisjoint(iterable)	         
7. issubset(iterable)	             
8. issuperset(iterable)	         
'''
# e.g.,

# Union (| or union())
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
print(fs1 | fs2)  
# Output: frozenset({1, 2, 3, 4, 5})

# Membership Testing:
# e.g.,

fs = frozenset([1, 2, 3])
print(2 in fs)
# Output: True
print(4 in fs)
# Output: False

# Frozenset vs. Set:

# Feature	                   Set	                                          Frozenset
'''
Mutability	     Mutable (can be modified).	                  Immutable (cannot be modified).
Hashable	     Not hashable (cannot be a dictionary key).	  Hashable (can be a dictionary key).
Operations	     Supports all set operations.	              Supports all read-only set operations.
Usage	         Used when modification is required.	      Used when immutability or hashability is required.
'''
# Use Cases of Frozensets:
# e.g.,

# Dictionary Keys: Frozensets can be used as keys in dictionaries since they are hashable.
fs = frozenset([1, 2, 3])
my_dict = {fs: "value"}
print(my_dict)  
# Output: {frozenset({1, 2, 3}): 'value'}

# Elements of Sets: A frozenset can be an element of another set.
fs = frozenset([1, 2])
my_set = {fs, 3}
print(my_set)  
# Output: {frozenset({1, 2}), 3}
