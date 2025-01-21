"                                                        🐍 Dictionaries in Python 🐍                                                                         "

# Python Dictionary:
'''
-> Dictionaries are used to store data values in key:value pairs.
-> Dictionaries are written with curly brackets, and have key and values which are separated by commas.
-> Dictionaries : Ordered, Changeable(mutable), indexed by keys, Keys(only hashable types) : value(any data type)
-> It is called as Mapping rather than sequences because it implements the concept of a "mapping" from mathematics and computer science where mapping 
refers to a collection of key:vlaue pairs.  
-> It has 11 built in methods
'''
# Syntax: my_dict = {key : value, key : value}

# Creating Dictionaries:

empty_dict = {}
print(empty_dict)
# Output: {}
print(type(empty_dict))
# Output: <class 'dict'>

empty_dict = dict()
print(empty_dict)
# Output: {}
print(type(empty_dict))
# Output: <class 'dict'>

my_dict = {"name":"Kobe Bryant", "age":23, "hobbies":["reading", "travelling"]}
print(my_dict)
# Output: {'name': 'Kobe Bryant', 'age': 23, 'hobbies': ['reading', 'travelling']}

my_dict = dict(name = "Kobe Bryant", age = 23, hobbies = ["reading", "travelling"])
print(my_dict)
# Output: {'name': 'Kobe Bryant', 'age': 23, 'hobbies': ['reading', 'travelling']}

my_list = ["name", "Kobe Bryant"] # list of strings
# my_dict = dict(my_list)
# Output: ValueError: dictionary update sequence element #0 has length 4; 2 is required

my_list = [["name", "Kobe Bryant"]] # list of list
my_dict = dict(my_list)
print(my_dict)
# Output: {'name': 'Kobe Bryant'}

my_tuple = (["name", "Kobe Bryant"],) # tuple of list
my_dict = dict(my_tuple)
print(my_dict)
# Output: {'name': 'Kobe Bryant'}

my_list = [("name", "Kobe Bryant"), ("age", 23)] # list of tuples
my_dict = dict(my_list)
print(my_dict)
# Output: {'name': 'Kobe Bryant', 'age': 23}

my_list = [("name", "Kobe Bryant"), ("age")]
# my_dict = dict(my_list)
# Output: ValueError: dictionary update sequence element #1 has length 3; 2 is required

my_list = ["name","age"]
my_tuple = ("Kobe Bryant", 23)
my_zip = zip(my_list, my_tuple)
print(my_zip)
# Output: <zip object at 0x000001DB34D1E900>
for i in my_zip:
    print(i)
# Output: ('name', 'Kobe Bryant')
#         ('age', 23)

my_dict = dict(zip(my_list, my_tuple))
print(my_dict)
# Output: {'name': 'Kobe Bryant', 'age': 23}

my_dict = dict(zip(my_tuple, my_list))
print(my_dict)
# Output: {'Kobe Bryant': 'name', 23: 'age'}

my_list = ["name","age"]
my_tuple = ("Kobe Bryant",)
my_dict = dict(zip(my_list, my_tuple))
print(my_dict)
# Output: {'name': 'Kobe Bryant'}

# Dictionary Indexing:

my_dict = {"brand":"Ford", "model":"Mustang", "year":1964}
print(my_dict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Accessing:

print(my_dict["brand"])
# Output: Ford

# print(my_dict["company"])
# Output: KeyError: 'company'

# Modifying:

my_dict["year"] = 2024
print(my_dict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2024}

my_dict["color"] = "red"
print(my_dict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2024, 'color': 'red'}

# Removing:

del my_dict["color"] # removes the item with the key name
print(my_dict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2024}

del my_dict # removes the dictionary completely
# print(my_dict)
# Output: NameError: name 'my_dict' is not defined

# Note: duplicate keys are not allowed
my_dict = {"brand":"Ford", "model":"Mustang", "year":1964, "brand":"Ferrari"}
print(my_dict)
# Output: {'brand': 'Ferrari', 'model': 'Mustang', 'year': 1964}

print(my_dict["brand"])
# Output: Ferrari

# Membership Checking:

my_dict = {"brand":"Ford", "model":"Mustang", "year":1964}

print("model" in my_dict)
# Output: True

print("Ford" in my_dict)
# Output: False

print("Ford" in my_dict.values())
# Output: True

# Dictionary Methods:

# 1. variable.get(keyname, value)

my_dict = {"brand":"Ford", "model":"Mustang", "year":1964}
print(my_dict.get("brand"))
# Output: Ford
print(my_dict.get("company", "does not exist"))
# Output: does not exist

# 2. variable.keys() --> It does not take any arguments

my_dict = {"brand":"Ford", "model":"Mustang", "year":1964}
print(my_dict.keys())
# Output: dict_keys(['brand', 'model', 'year'])

# 3. variable.value() --> It does not take any arguments

my_dict = {"brand":"Ford", "model":"Mustang", "year":1964}
print(my_dict.values())
# Output: dict_values(['Ford', 'Mustang', 1964])

# 4. variable.items() --> It does not take any arguments

my_dict = {"brand":"Ford", "model":"Mustang", "year":1964}
print(my_dict.items())
# Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# 5. variable.update(iterable with key:value)

my_dict = {"brand":"Ford", "model":"Mustang", "year":1964}
my_dict.update({"year":2024})
print(my_dict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2024}

my_dict.update([["color","red"]])
print(my_dict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2024, 'color': 'red'}

my_dict.update(speed = "220 kmph", industry = "automobile")
print(my_dict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2024, 'color': 'red', 'speed': '220 kmph', 'industry': 'automobile'}

# 6. variable.pop(key name, default value)

my_dict = {"brand":"Ford", "model":"Mustang", "year":1964}
print(my_dict.pop("model"))
# Output: Mustang
print(my_dict)
# Output: {'brand': 'Ford', 'year': 1964}

# print(my_dict.pop("company"))
# Output: KeyError: 'company'

print(my_dict.pop("company", "does not exist"))
# Output: does not exist

# 7. variable.popitem() --> It does not take any arguments

my_dict = {"brand":"Ford", "model":"Mustang", "year":1964}
print(my_dict.popitem())
# Output: ('year', 1964)
print(my_dict)
# Output: {'brand': 'Ford', 'model': 'Mustang'}

my_dict = {}
# my_dict.popitem()
# KeyError: 'popitem(): dictionary is empty'

# 8. variable.clear() --> It does not take any arguments

my_dict = {"brand":"Ford", "model":"Mustang", "year":1964}
my_dict.clear()
print(my_dict)
# Output: {}

# 9. variable.copy() --> It does not take any arguments

my_dict1 = {"a":1, "b":2, "c":3}
my_dict2 = my_dict1
my_dict1["d"] = 4
print(my_dict1)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(my_dict2)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

my_dict1 = {"a":1, "b":2, "c":3}
my_dict2 = my_dict1.copy()
my_dict1["d"] = 4
print(my_dict1)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(my_dict2)
# {'a': 1, 'b': 2, 'c': 3}

# 10. variable = dict.fromkeys(keys, value)

keys = ("key1", "key2", "key3")
value = 0
my_dict = dict.fromkeys(keys, value)
print(my_dict)
# Output: {'key1': 0, 'key2': 0, 'key3': 0}

keys = ("key1", "key2", "key3")
value = (0,1)
my_dict = dict.fromkeys(keys, value)
print(my_dict)
# Output: {'key1': (0, 1), 'key2': (0, 1), 'key3': (0, 1)}

my_dict = dict.fromkeys({"a":1})
print(my_dict)
# Output: {'a': None}

my_dict = dict. fromkeys(["a",1])
print(my_dict)
# Output: {'a': None, 1: None}

# 11. variable.setdefault(key name, value)

my_dict = {"name":"Kobe", "age":23, "height": 6.0}
my_dict.setdefault("age", 30)
print(my_dict)
# Output: {'name': 'Kobe', 'age': 23, 'height': 6.0}

my_dict.setdefault("weight", 75)
print(my_dict)
# Output: {'name': 'Kobe', 'age': 23, 'height': 6.0, 'weight': 75}

# Loop through Dictionaries:

my_dict = {"brand":"Ford", "model":"Mustang", "year":1964}
for i in my_dict:
    print(i)
# Output: brand
#         model
#         year

for i in my_dict:
    print(my_dict[i])
# Output: Ford
#         Mustang
#         1964

# Using dictionary methods:
for i in my_dict.keys():
    print(i)
# Output: brand
#         model
#         year

for i in my_dict.values():
    print(i)
# Output: Ford
#         Mustang
#         1964

for i in my_dict.items():
    print(i)
# Output: ('brand', 'Ford')
#         ('model', 'Mustang')
#         ('year', 1964)

for i,j in my_dict.items():
    print(i,j)
# Output: brand Ford
#         model Mustang
#         year 1964

# Nested Dictionary:
'''
-> Dictionaries inside a dictionary is called nested dictionaries.
'''
# e.g.,

my_details = {
    "name":"Kobe Bryant",
    "age": 23,
    "interest": ["cricket", "hockey"]
}
print(my_details)
# Output: {'name': 'Kobe Bryant', 'age': 23, 'interest': ['cricket', 'hockey']}
print(my_details["interest"][0])
# Output: cricket

my_family = {
    "child1":{"name":"Ram", "year": 2004},
    "child2":{"name":"Krishna", "year": 2007},
    "child3":{"name":"Venkat", "year": 2011}
}
print(my_family)
# Output: {'child1': {'name': 'Ram', 'year': 2004}, 'child2': {'name': 'Krishna', 'year': 2007}, 'child3': {'name': 'Venkat', 'year': 2011}}

child1 = {"name":"Ram", "year": 2004}
child2 = {"name":"Krishna", "year": 2007}
child3 = {"name":"Venkat", "year": 2011}

my_family = {
    "child1":child1,
    "child2":child2,
    "child3":child3
}
print(my_family)
# Output: {'child1': {'name': 'Ram', 'year': 2004}, 'child2': {'name': 'Krishna', 'year': 2007}, 'child3': {'name': 'Venkat', 'year': 2011}}

print(my_family["child1"]["name"])
# Output: Ram

# Loop through Nested Dictionary:
for x, obj in my_family.items():
    print(x)
    for y in obj:
        print(y + ":", obj[y])

# Output: child1
#         name: Ram
#         year: 2004
#         child2
#         name: Krishna
#         year: 2007
#         child3
#         name: Venkat
#         year: 2011

# Dictionary Comprehension:
'''
-> We can also create a dictionary using comprehension (based on the expression, the dictionary will be created).
'''
my_dict = {x : x ** 2 for x in range(6)}
print(my_dict)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

my_dict = {x : x ** 2 for x in range(6) if x % 2 == 0}
print(my_dict)
# Output: {0: 0, 2: 4, 4: 16}

my_set = {x ** 2 for x in range(6)}
print(my_set)
# Output: {0, 1, 4, 9, 16, 25}

# Dictionary Concatenation and Repetition:
'''
-> In Python, dictionaries do not natively support + (concatenation) or * (repetition) like lists do. 
-> If you attempt to use these operators directly on dictionaries, it will raise a TypeError. 
-> However, you can simulate concatenation and repetition behavior with custom logic.
'''
# e.g.,

# 1. Dictionary Concatenation:

dict1 = {"name":"Kobe Bryant"}
dict2 = {"age":23}
# dict3 = dict1 + dict2
# Output: TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# Different Ways:

# Using | Operator (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# Concatenation
result = dict1 | dict2
print(result)  
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using update() Method
dict1.update(dict2)
print(dict1)  
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Use dictionary unpacking (**) to merge dictionaries.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# Simulated Concatenation
result = {**dict1, **dict2}
print(result)  
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Create a custom function to simulate the + operator
def dict_concat(d1, d2):
    return {**d1, **d2}

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
result = dict_concat(dict1, dict2)

print(result) 
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 2. Dictionary Repetition:

original_dict = {"a": 1, "b": 2}
# print(original_dict * 2)
# Output: TypeError: unsupported operand type(s) for *: 'dict' and 'int'

# Different Ways:

# Repeating Key-Value Pairs
repeated_dict = {f"{key}_{i}": value for i in range(3) for key, value in original_dict.items()}
print(repeated_dict)
# Output: {'a_0': 1, 'b_0': 2, 'a_1': 1, 'b_1': 2, 'a_2': 1, 'b_2': 2}

# Repeat the dictionary in a list
repeated_list = [original_dict.copy() for _ in range(3)]
print(repeated_list)
# Output: [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}]
