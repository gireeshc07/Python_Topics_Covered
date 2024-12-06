
# Python Constants:
'''
-> In Python, constants are variables that are intended to remain unaltered during program execution.
-> Unlike some other languages, Python does not have a keyword or mechanism to define immutable constants, so they rely on conventions and 
   sometimes additional tools for enforcement.'''

# How Constants are Defined in Python:

# 1. Naming Convention:
'''
-> In Python, constants are conventionally defined using all uppercase letters, with underscores (_) separating words. This makes them easily 
   recognizable in the code.
   
Example:'''

PI = 3.14159
MAX_CONNECTIONS = 100
APP_NAME = "MyApp"
'''
-> These variables are constants by developer agreement. Python won't stop you from reassigning them (e.g., PI = 3), but this violates the purpose 
   and convention of constants.'''

# 2. Modules for Constants:
'''
-> Constants are often defined in a separate module (file), typically named something like constants.py. This approach helps organize the code, 
   prevents hardcoding values, and makes constants easy to locate and manage.
   
Example:'''

# constants.py
API_URL = "https://api.example.com"
DEFAULT_TIMEOUT = 30

# main.py
# import constants
# print(constants.API_URL)

# Why Python Doesn't Enforce Constants?
'''
-> Unlike languages like C++ (const) or Java (final), Python is a dynamically typed language and follows the principle of "consenting adults" 
   —developers are trusted to respect conventions instead of the language enforcing strict rules.
   
For Example:'''

PI = 3.14159  # Intended as a constant
PI = 3  # Python allows reassignment, but it is considered a bad practice!

# Workarounds to Enforce Constants(optional):
'''
-> While Python lacks built-in support for immutable constants, it offers several workarounds to simulate immutability. Here’s a detailed 
   explanation of how these methods can be used to define constants:'''

# 1. Using namedtuple for Constants:
'''
-> The namedtuple is a class from Python's collections module. It creates an immutable object where attributes are accessed by name, making it a 
   suitable option for grouping constants.

Why Use namedtuple?
-> It provides immutability (attributes can’t be reassigned).
-> Allows grouping related constants logically.
-> Lightweight and simple to use.

Example:'''

"Step 1: Define a namedtuple for your constants"

from collections import namedtuple

# Define a namedtuple
Constants = namedtuple("Constants", ["PI", "GRAVITY", "SPEED_OF_LIGHT"])

# Initialize constants
scientific_constants = Constants(PI=3.14159, GRAVITY=9.8, SPEED_OF_LIGHT=299792458)

"Step 2: Access constants as attributes"

# Access constants
print(scientific_constants.PI)  # Output: 3.14159
print(scientific_constants.GRAVITY)  # Output: 9.8

# Attempting to modify a constant raises an error
# scientific_constants.PI = 3.14  # AttributeError: can't set attribute

"Step 3: Group related constants"

# Example: Physics constants
PhysicsConstants = namedtuple("PhysicsConstants", ["PLANCK_CONSTANT", "LIGHT_SPEED"])
physics_constants = PhysicsConstants(PLANCK_CONSTANT=6.626e-34, LIGHT_SPEED=3e8)

print(physics_constants.LIGHT_SPEED)  # Output: 300000000.0

# 2. Using dataclass for Constants:
'''
-> The dataclass decorator in Python allows defining classes with minimal boilerplate code. By setting the frozen=True argument, you can make a 
   dataclass immutable, which is ideal for constants.

Why Use dataclass?
-> Provides a structured and readable way to group constants.
-> Supports immutability when frozen=True is used.
-> Useful for more complex constants with default values or validation.

Example:'''

"Step 1: Create a dataclass with frozen=True"

from dataclasses import dataclass

@dataclass(frozen=True)  # Makes the dataclass immutable
class MathConstants:
    PI: float = 3.14159
    E: float = 2.71828
    GOLDEN_RATIO: float = 1.61803

"Step 2: Instantiate and use"

constants = MathConstants()
print(constants.PI)  # Output: 3.14159
print(constants.E)   # Output: 2.71828

# Attempting to modify raises an error
# constants.PI = 3.14  # Raises FrozenInstanceError

"Step 3: Organize complex constants"
"-> If your constants have multiple related values:"

@dataclass(frozen=True)
class Config:
    API_KEY: str = "12345-ABCDE"
    TIMEOUT: int = 30  # seconds
    BASE_URL: str = "https://api.example.com"

config = Config()
print(config.BASE_URL)  # Output: https://api.example.com

# 3. Using a Custom Class for Constants:
'''
-> Custom classes can be used to define constants with a clear structure. By overriding the __setattr__ method, you can prevent reassignment of 
   class-level attributes.

Why Use a Custom Class?
-> Provides flexibility in how constants are accessed.
-> Can be used for logical grouping and organization.
-> Immutability can be enforced by overriding methods.

Example:'''

"Step 1: Define a class and constants as attributes"
class AppConstants:
    # Define constants as class attributes
    APP_NAME = "MyApp"
    VERSION = "1.0.0"
    SUPPORT_EMAIL = "support@example.com"
    
    # Prevent reassignment by overriding __setattr__
    def __setattr__(self, key, value):
        raise AttributeError("Constants cannot be modified.")

"Step 2: Access constants"
constants = AppConstants()
print(constants.APP_NAME)  # Output: MyApp
print(constants.VERSION)   # Output: 1.0.0

# Attempting to modify raises an error
# constants.VERSION = 2.0.0  # Raises AttributeError

"Step 3: Use classes for logical grouping"
class HTTPStatusCodes:
    OK = 200
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

print(HTTPStatusCodes.OK)  # Output: 200

# 4. Using MappingProxyType for Constants:
'''
-> The MappingProxyType from the types module creates a read-only view of a dictionary. This is a simple way to ensure constants stored in a 
   dictionary cannot be modified.

Why Use MappingProxyType?
-> Ideal for grouping constants in a dictionary format.
-> Enforces immutability by preventing updates to the dictionary.

Example:'''
 
"Step 1: Define a dictionary and wrap it with MappingProxyType"
from types import MappingProxyType

# Define a dictionary for constants
constants_dict = {
    "PI": 3.14159,
    "E": 2.71828,
    "GOLDEN_RATIO": 1.61803
}

# Make it immutable
CONSTANTS = MappingProxyType(constants_dict)

"Step 2: Access constants like a dictionary"
print(CONSTANTS["PI"])  # Output: 3.14159

"Step 3: Attempting to modify results in an error"
# CONSTANTS["PI"] = 3.14  # TypeError: 'mappingproxy' object does not support item assignment

# When to Use Which Method?

# 1. Use namedtuple:
'''
-> When you need a lightweight and immutable collection of constants.
-> For simple constants like physics values or configurations.'''

# 2. Use dataclass:
'''
-> When constants have multiple attributes or need default values.
-> When you want a more organized and readable structure.'''

# 3. Use a Custom Class:
'''
-> When you need flexibility in accessing constants.
-> For logically grouping constants while enforcing immutability.'''

# 4. Use MappingProxyType:
'''
-> When constants are naturally represented as key-value pairs.
-> When you want a lightweight, read-only dictionary for constants.'''

# Good Practices for Using Constants:

# 1. Follow Naming Conventions:
'''
-> Use UPPERCASE_WITH_UNDERSCORES for constants.

e.g.'''

MAX_USERS = 100
BASE_URL = "https://example.com"

# 2. Group Constants Together:
'''
-> Organize constants in a single module (constants.py) or inside a class.

e.g.'''

# constants.py
MAX_USERS = 100
DEFAULT_LANGUAGE = "en"

# 3. Document Constants:
'''
-> Use comments or docstrings to explain the purpose of constants, especially if the name isn’t self-explanatory.

e.g.'''

SPEED_OF_LIGHT = 299792458  # Speed of light in meters per second

# 4. Avoid Redefining Constants:
'''
-> Do not reassign values to constants after defining them. While Python allows it, this violates the intent.

e.g.'''

PI = 3.14159
PI = 3.14  # Bad practice!

# 5. Use Constants for Readability:
'''
-> Replace magic numbers or hardcoded strings with named constants.

e.g.'''

attempts=5

# Bad:
if attempts > 3:
    print("Too many attempts")

# Good:
MAX_ATTEMPTS = 3
if attempts > MAX_ATTEMPTS:
    print("Too many attempts")
    
# 6. Use Tools to Enforce Immutability:
'''
-> If you want to ensure constants aren’t modified, use one of the techniques described earlier, like dataclass or MappingProxyType.'''
