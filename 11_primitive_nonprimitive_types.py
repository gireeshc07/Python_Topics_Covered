
# 1. Primitive(or Simple) Data Types:
'''
-> Primitive data types are the basic building blocks of data in Python. 
-> They represent simple, atomic values and are not composed of other data types. 
-> They are directly supported by Python and are immutable (cannot be changed after they are created).  
'''
# e.g.,

# 1. Integers (int)
# 2. Floating-point Numbers (float)
# 3. Complex Numbers
# 4. Booleans (bool)
# 5. Strings (str)
# 6. NoneType (None)

# Key Characteristics of Primitive:

# 1. Atomic Nature: Represent a single value.

# Example: int (e.g., 5), float (e.g., 3.14), bool (e.g., True), and str (e.g., "Hello").

# 2. Built-In: Provided by the language itself, with no need for user-defined structures.

# 3. Simple and Easy to Use : Straightforward in syntax and behavior.
# e.g.,
x = 10  # Integer
y = "Python"  # String
z = True  # Boolean

# 4. Immutable: Once a value is assigned to a variable, its literal value cannot be changed (though the variable can be reassigned).
# e.g.,
x = 10
x = 20  # Reassigns x; does not modify the original value 10.

# 5. Efficient for Basic Operations: Used for basic calculations and simple data storage.
# e.g.,
a = 5
b = 3.2
result = a + b  # Output: 8.2

# 6. Predefined Behavior:
'''
-> Each primitive type in Python has predefined behavior 
   - Integers (int): Represent whole numbers and support mathematical operations.
   - Floating-Point Numbers (float): Represent real numbers with decimal points and follow IEEE 754 standards.
-> In Python, primitive types do not have a fixed size but have consistent behavior.
-> This flexibility is one of Python's strengths, making it easier to handle large numbers or high-precision calculations without worrying about data overflow.
'''
# e.g.,
x = 12345678901234567890  # Python allows arbitrarily large integers.
y = 3.14159  # A float representing a real number.

# Comparison with Other Languages:
'''
-> In languages like C, an int or float has a fixed size and behavior:
   - C int: Typically 4 bytes (32 bits).
   - C float: Typically 4 bytes (32 bits), with limited precision.'''

# 2. Non-Primitive(or Complex) Data Types:
'''
-> Non-primitive data types are more complex structures that can be created using primitive data types. 
-> They are mutable (most of the time) and can store multiple values or complex objects.'''

# e.g.,

# 1. Lists
# 2. Tuples
# 3. Sets
# 4. Dictionaries
# 5. Range
# 6. Binary Types (bytes, bytearraya, memoryviewa)
# 7. Strings (Advanced Use): Strings can also act as non-primitive when used with slicing, concatenation, or iteration.
# e.g.,
message = "Python"
for char in message:
   print(char,end=" ")  # Iterates over each character
# Output: P y t h o n 

# 8. User-Defined Classes and Objects: Structures defined by the user using the class keyword.
# e.g.,
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

p = Person("Alice", 30)  # Object of the Person class

# 9. Complex Data Structures:
'''
-> Python also supports more advanced data structures built using the primitive and non-primitive types:
  - Stacks: Implemented using list or deque.
  - Queues: Implemented using deque or queue.Queue.
  - Graphs: Represented using dictionaries.
  - Trees: Implemented using custom classes.'''

# Key Characteristics:

# 1. Can Store Multiple Values: Represent collections or relationships between values.  
# e.g.,
# - list (e.g., [1, 2, 3])
# - dict (e.g., {"name": "Alice", "age": 30})

# 2. User-Defined and Built-In:
'''
-> Python provides built-in non-primitive types like list, tuple, dict, set, etc.  
-> Users can define their own types using classes.'''

# 3. Dynamic in Size: Unlike primitive types, non-primitive types like lists and dictionaries can dynamically grow or shrink.
# e.g.,
fruits = ["apple", "banana"]
fruits.append("cherry")  # Adds "cherry" to the list

# 4. Can Be Mutable or Immutable: Some non-primitive types are mutable (e.g., list, dict), while others are immutablen (e.g., tuple, frozenset).

# 5. Complex Structures: Can represent more complex relationships, such as key-value pairs or hierarchical data.
# e.g.,
person = {
   "name": "Alice",
   "age": 30,
   "hobbies": ["reading", "traveling"]
}

# 6. Supports Advanced Operations: Non-primitive types allow methods for searching, sorting, indexing, etc.
# e.g.,
numbers = [5, 2, 9]
numbers.sort()  # Sorts the list in ascending order

# 7. Essential for Data Structures and Algorithms: Non-primitive types are key for implementing advanced data structures like stacks, queues, and trees.

# Real-World Analogy:
'''
-> Primitive Data Types: Think of a single book. It represents one piece of information (e.g., an integer or a string).
-> Non-Primitive Data Types: Think of a bookshelf. It holds multiple books (e.g., a list or dictionary) and organizes them for efficient access and use.
'''
# Key Differences Between Primitive and Non-Primitive Data Types:
'''
| Feature                     | Primitive Data Types                       | Non-Primitive Data Types                         |
|-----------------------------|--------------------------------------------|--------------------------------------------------|
| Definition                  | Basic building blocks of data.             | Complex structures built using primitives.       |
| Examples                    | int, float, bool, str                      | list, tuple, dict, set                           |
| Storage                     | Store single, atomic values.               | Store multiple or structured values.             |
| Size                        | Predefined behavior                        | Can grow or shrink dynamically.                  |
| Mutability                  | Immutable.                                 | Mutable (e.g., list) or Immutable (e.g., tuple). |
| Built-In/User-Defined       | Always built-in.                           | Can be built-in or user-defined (e.g., classes). |
| Complexity                  | Simple and straightforward.                | More complex and flexible.                       |
| Operations                  | Limited to basic operations(e.g., +, -, *).| Advanced operations like sorting, indexing, etc. |
| Use Cases                   | Basic calculations, simple storage.        | Data organization, advanced algorithms.          |'''

# Why Is Understanding Primitive and Non-Primitive Types Important?

# 1. Efficient Memory Management: Primitive types consume less memory, whereas non-primitives often involve additional memory allocation for their structure.

# 2. Optimized Operations: Primitive types are faster for simple tasks (e.g., arithmetic), while non-primitives are ideal for managing complex data.

# 3. Flexibility in Data Modeling: Non-primitives allow storing and manipulating data in real-world applications, like managing customer information using dictionaries.

# 4. Prevention of Errors: Knowing when to use primitives or non-primitives helps avoid bugs. For example, using a tuple for fixed data ensures immutability.

# Real-Life Examples:

# Example-1
# Primitive Data Types
balance = 1000.50  #  A bank account balance (float)
age = 30  #  A user's age (int)
is_logged_in = True  #  A login status (bool)

# Non-Primitive Data Types
transactions = [200, -50, 300]  #  A list of transactions (list)
customer = {"name": "Alice", "age": 30, "balance": 1000.50}  #  Customer details (dict)

# Example-2
# Primitive Data Type
# A coffee shop stores the price of a single coffee as:
price = 5 # int
  
# Non-Primitive Data Type
# A coffee shop stores details about orders as a list of dictionaries:
orders = [
   {"customer": "Alice", "drink": "Latte", "price": 5},
   {"customer": "Bob", "drink": "Espresso", "price": 3}
]
