
# Hashable and Unhashable Objects in Python:
'''
-> In Python, objects are classified as hashable or unhashable based on their mutability and their ability to be used as keys in dictionaries or elements in sets.
'''
# Hashable Objects:
'''
1. Has a hash value: It must have a fixed hash value for its lifetime, which is calculated using the hash() function.
2. Immutable: Its state (data) cannot change after it is created.
3. Comparable: Hashable objects can be compared for equality (==) to determine if they are the same.
4. Can be used as dictionary keys or set elements: Hashable objects are suitable for these data structures because their immutability ensures consistent behavior.
'''
# Examples of Hashable Objects:
'''
- Numbers: int, float, complex
- Strings: 'Hello', "World"
- Tuples: (1, 2, 3) (only if all elements in the tuple are also hashable)
- Booleans: True, False
- NoneType: None
- range()
- frozenset()
'''
# e.g.,

# Numbers
print(hash(42))  # Output: 42 A unique integer

# Strings
print(hash("Python"))  # Output: 1358852976584445598 Hash value for the string

# Tuples # Tuples are hashable if they contain only hashable elements
print(hash((1, 2, 3)))  # Output: 529344067295497451 Hash value for the tuple

# Hashing a range object
r = range(1, 10, 2)
print(hash(r))  # Outputs a hash value

# Using range as a dictionary key
d = {range(1, 5): "Range 1 to 5"}
print(d[range(1, 5)])  # Outputs: "Range 1 to 5"

# Storing range in a set
s = {range(1, 5), range(5, 10)}
print(s)  # Outputs: {range(1, 5), range(5, 10)}

# Unhashable Objects:
'''
1. Cannot have a fixed hash value: Because its contents can change, the hash value would not be reliable.
2. Mutable: Its state (data) can be modified after creation.
3. Cannot be used as dictionary keys or set elements: Using unhashable objects in these data structures would break consistency and cause errors.
'''
# Examples of Unhashable Objects:
'''
- Lists: [1, 2, 3]
- Dictionaries: {'a': 1, 'b': 2}
- Sets: {1, 2, 3}
'''
# e.g.,

# Attempting to hash mutable types raises a TypeError
my_list = [1, 2, 3]
# print(hash(my_list))  # Raises TypeError: unhashable type: 'list'

my_dict = {"key": "value"}
# print(hash(my_dict))  # Raises TypeError: unhashable type: 'dict'

# Key Differences Between Hashable and Unhashable Objects:
'''
| Feature                | Hashable Objects                | Unhashable Objects             |
|------------------------|---------------------------------|--------------------------------|
| Mutability             | Immutable                       | Mutable                        |
| Hash Value             | Has a fixed hash value          | No hash value                  |
| Examples               | Numbers, strings, tuples        | Lists, dictionaries, sets      |
| Usage in Dict/Set      | Can be used as keys/elements    | Cannot be used as keys/elements|
| Hash Function          | Works with hash()               | Raises TypeError               |'''

# Why Does Python Enforce This?
'''
1. Consistency: Hashable objects must maintain a consistent hash value to allow quick lookup in hash-based data structures (e.g., dictionaries and sets).
2. Efficiency: Hash-based structures rely on the hash value to determine where to store or retrieve objects. If the hash value changes due to mutability, it would break the structure.
'''
# How to Make Custom Objects Hashable:
'''
-> You can create a custom hashable object by overriding the __hash__() and __eq__() methods in a class.'''

# Example
class HashableObject:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)  # Use the hash of the internal value

    def __eq__(self, other):
        return isinstance(other, HashableObject) and self.value == other.value

# Usage
obj1 = HashableObject(42)
obj2 = HashableObject(42)
print(hash(obj1))  # Output: consistent hash value
print(obj1 == obj2)  # Output: True

# Summary:
'''
-> Hashable objects are immutable and have a fixed hash value, making them suitable for use as keys in dictionaries or elements in sets.
-> Unhashable objects are mutable and lack a fixed hash value, preventing their use in hash-based data structures.
-> Python enforces these rules to maintain the integrity and efficiency of data structures like dictionaries and sets.
'''

# Hash Value:
'''
-> A hash value is a fixed-size number that uniquely represents an object(data). 
-> The hash() function is a built-in Python function that takes an object and calculates a hash value for it. 
-> Think of a hash value as a special number or code that uniquely represents an object, but instead of having to remember the entire object, you just remember this code.
'''
# Uses of Hash Values:

# Efficient Data Lookups: This hash value is an integer, and it helps in efficient storage and retrieval of objects in 
# hash-based data structures like dictionaries and sets.
# Quick Comparisons: Efficiently compare objects without inspecting full data.
# Data Integrity: Ensure data hasn't changed, particularly in cryptographic applications.

# Real-Life Example: Locker Numbers
'''
-> Imagine you are in a school with hundreds of students. Instead of remembering each student's name, grade, or all their details, the school assigns each student a locker number.

   - Locker number is like a hash value.
   - Student's details (like name, age, etc.) are like the object.
   - The locker number is unique for every student, just like a hash value is unique for a specific object.

-> So, when you want to find out where a student’s information is stored, you just remember the locker number (hash value), and it leads you directly to that student's details. 
   You don’t need to remember everything about them, just the locker number.
'''
# Key Characteristics of a Hash Value:
'''
1. Deterministic: If you give the same input (data), you'll always get the same hash value in one program run.
2. Fixed Size: The hash value is always an integer of a fixed size, regardless of how large or small the original data is.
3. Uniqueness: Ideally, different inputs produce different hash values. However, there’s always a chance for a hash collision, where different inputs give the same hash value.
4. Immutable Objects: Only immutable objects (e.g., numbers, strings, tuples) can generate reliable hash values. Mutable objects (like lists or dictionaries) cannot reliably 
   generate hash values, because their data can change.
'''
# Common Use Cases:

# 1. Key in Dictionaries:
'''
-> The hash value of a key determines where it is stored in the dictionary.'''
# e.g.,
my_dict = {1: "one", 2: "two"}
print(hash(1))  # Hash value of the key

# 2. Membership Testing in Sets:
'''
-> Sets use hash values to check membership efficiently.'''
# e.g.,
my_set = {1, 2, 3}
print(hash(2) in my_set)  # Fast lookup using hash

# hash() Function:
'''
-> The hash() function in Python is a built-in function that returns the hash value of an object. 
-> A hash value is an integer uniquely representing the given object, which is computed using a hashing algorithm. 
-> It works only with immutable objects (e.g., numbers, strings, tuples) and is used in data structures like dictionaries and sets for efficient data lookup.
'''
# Syntax: hash(object)

# object: The input can be any object that is hashable. 
# A hashable object is one that has a defined __hash__() method and is immutable, such as numbers, strings, or tuples.

# Real-Life Example: Generating Locker Numbers
'''
-> Let’s say you want to create a system where each student is assigned a locker number. 

   - You might decide that every student gets a number based on the letters in their name. For example, the first letter 
     of the name could be converted into a number, then the next letter, and so on.
   - The hash() function does something similar. It takes an object (like a string "Python") and creates a number 
     (hash value) based on the content of that object.

-> If you pass the string "Python" to hash(), Python will calculate a number that is unique to "Python". So every time you run the hash() function on the word "Python", it will 
   always give you the same number during the same program run.
'''
# How the hash() function works:
'''
1. Input: You give the hash() function an object.
2. Processing: Python applies a special algorithm to the object and turns it into a number.
3. Output: You get a hash value (a unique integer) for that object.
'''
# e.g.,
# Hashing a Number:
print(hash(42))
# Output: 42

# Hashing a String:
print(hash("Python"))
# Output: 2220277995051760824

# Hashing a Tuple:
print(hash((1, 2, 3)))
# Output: 529344067295497451 

# Attempting to Hash Unhashable Objects
my_list = [1, 2, 3]
# print(hash(my_list))  # Raises TypeError: unhashable type: 'list'

# Important Notes on Hashing:

# 1. Hash Collisions:
'''
-> A hash collision occurs when two different inputs (objects) produce the same hash value. 
-> This can happen because the range of possible hash values is finite, but the number of possible input values is practically infinite.
-> When two different objects produce the same hash value, Python handles this situation efficiently using techniques like chaining or open addressing in hash-based data structures 
   like dictionaries and sets.
'''
# Example of Hash Collision

# Hashing two strings
hash1 = hash("apple")
hash2 = hash("banana")

print(f"Hash of 'apple': {hash1}")
print(f"Hash of 'banana': {hash2}")

# Output (values will differ in your case, but for explanation, let's assume they both output the same hash):

# Hash of 'apple': 123456789
# Hash of 'banana': 123456789

# As you can see, even though "apple" and "banana" are different, they have the same hash value. This is called a hash 
# collision.

# How Python Handles Hash Collisions:
'''
-> Python uses chaining or open addressing to handle hash collisions in dictionaries and sets:

   - Chaining: If two objects have the same hash value, Python stores them in a linked list or another structure at that hash location.
   - Open Addressing: If there’s a collision, Python looks for the next available slot in the table and stores the new object there.

-> This makes sure that Python can still store and retrieve objects efficiently, even if hash collisions occur.
'''
# 2. Hash Randomization:
'''
-> Starting from Python 3.3, Python introduced hash randomization as a security feature. This means that the hash value for strings (and some other objects) will differ between 
   program runs. 
-> The reason for this is to prevent attackers from using predictable hash values in certain security scenarios, such as hash collisions in hash tables or dictionaries.
'''
# Example of Hash Randomization

# Hashing the string "hello" multiple times
print(hash("hello"))
print(hash("hello"))

# In Python 3.3 and later, if you run the same code multiple times, the output will change each time:

# First run:
# - Hash of "hello": 1234567890

# Second run:
# - Hash of "hello": 9876543210

# The hash values for the string "hello" are different in each run. This is because Python randomizes the hash values 
# between different program runs to enhance security.

# If you're using an older version of Python (before 3.3), the hash value for the same input will always be the same in 
# every program run.

# 3. Hash and Equality Rule:
'''
-> In Python, there’s an important rule that if two objects are considered equal, then their hash values must also be equal. 
-> This rule is important for the proper functioning of data structures like dictionaries and sets.
-> However, the reverse is not necessarily true —two objects with the same hash value might not always be equal. 
-> This means that even if two objects have the same hash, they could still be different objects.
'''
# Example: Hash and Equality

# Two strings that are equal in value
a = "hello"
b = "hello"

# Check if they are equal
print(a == b)  # Output: True

# Check if their hash values are equal
print(hash(a) == hash(b))  # Output: True

# Here, both strings a and b have the same content "hello", so they are equal and their hash values are also the same.

# Example: Same Hash Value but Not Equal

class MyClass:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return 42  # Same hash value for any object of this class

obj1 = MyClass(1)
obj2 = MyClass(2)

# Check if they are equal
print(obj1 == obj2)  # Output: False (because 1 != 2)

# Check if their hash values are equal
print(hash(obj1) == hash(obj2))  # Output: True (since both return 42)
'''
-> Equality (obj1 == obj2): Here, obj1 and obj2 are not equal because their internal values (1 and 2) are different.
-> Hash Values (hash(obj1) == hash(obj2)): Despite being unequal, the hash values for both objects are the same because we manually defined their hash function to always return 42.
'''
# Why this Matters?
'''
-> The equality check (obj1 == obj2) ensures that objects with the same content are treated as equal.
-> The hash values need to match for equal objects so that Python can store and compare them efficiently (especially in sets and dictionaries).
-> Objects with the same hash value but different content should not be considered equal, which is why Python allows this difference.

These concepts are essential for working with data structures like dictionaries and sets, ensuring that Python can efficiently store, retrieve, and compare objects.
'''
# Why is Hashing Important?

# 1. Efficient Lookups (Finding Things Quickly):
'''
-> Imagine a large library with thousands of books. If you had to look for a book by reading through each one, it would take forever!
-> Instead, libraries use book IDs (like a hash value) to quickly find any book.
-> In the same way, Python uses hash values to quickly find things in dictionaries or sets. The hash() function helps Python find the correct place to store or look up data.
'''
# 2. Comparing Objects:
'''
-> If you have two objects (like two different students), you don’t need to compare all their details. You can just compare their locker numbers (hash values). 
   If the locker numbers are the same, the students must be the same.
-> This is how Python compares objects: It compares their hash values to check if they are the same or not.
'''
# Real-Life Example: Hashing in Action
'''
Imagine a bank database where people’s account information is stored. Each person has a unique account number, which is like a hash value for that person’s account. 

-> If someone wants to withdraw money, they can give their account number (hash value) to the bank, and the bank will quickly find the correct account using that number.
-> The account number is like the result of the hash() function applied to the person's details.
'''
# Summary:
'''
-> A hash value is like a unique locker number that represents an object.
-> The hash() function is like a tool that creates that locker number based on the object you give it.
-> It’s used to quickly find, compare, and store data in systems like dictionaries and sets in Python.

Just like you use locker numbers to quickly find a student's belongings in school, Python uses hash values to quickly access and manage data.
'''