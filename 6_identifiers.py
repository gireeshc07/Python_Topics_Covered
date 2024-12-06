
# Identifiers in Python
'''
-> An identifier in Python is the name used to identify variables, functions, classes, modules, or other objects. 
-> It acts as a reference for the value or object stored in memory.'''

# Rules for Naming Identifiers
'''
1. Identifiers can contain letters (a-z, A-Z), digits (0-9), and underscores (_).

2. Identifiers cannot contain special characters like @, #, $, etc.

3. An identifier cannot begin with a number.

4. Identifiers are case-sensitive, meaning Variable and variable are treated as two different identifiers.

5. You cannot use Python's reserved keywords (like if, for, class, etc.) as identifiers.

6. Identifiers cannot have spaces. Use underscores _ to separate words.'''

# Types of Identifiers:
'''
1. Variables --> Names used to store data values (snake_case)
2. Functions --> Names used to refer to functions or methods (snake_case)
3. Classes --> Names for class definitions (snake_case)
4. Modules --> Names for modules you import in your code (snake_case)
5. Constants --> Names for constant values (SCREAMING_SNAKE_CASE)'''

# Identifier Cases in Python
'''
Python allows identifiers to follow different naming conventions, each designed for specific use cases. These cases improve code readability and convey the purpose of the identifier.
'''
# 1. Snake Case
'''
-> Words are written in lowercase and separated by underscores (_).
-> Commonly used for variables, function names, and module names.
Examples:'''

variable_name = 10
def calculate_area(radius):
    return 3.14 * radius ** 2

# 2. Pascal Case (Camel Case with Uppercase Start)
'''
-> Each word starts with an uppercase letter, with no underscores.
-> Used for class names.
Examples:'''

class Circle:
    pass

class StudentDetails:
    pass

# 3. Camel Case
'''
-> Similar to Pascal Case, but the first word starts with a lowercase letter.
-> Not a common convention in Python but seen in some frameworks and libraries.
Examples:'''

studentName = "Alice"
calculateArea = lambda radius: 3.14 * radius ** 2

# 4. SCREAMING_SNAKE_CASE(UPPERCASE_WITH_UNDERSCORES)
'''
-> All letters are uppercase, with words separated by underscores (_).
-> Used for constants or global variables.
Examples:'''

PI = 3.14159
MAX_CONNECTIONS = 100

# 5. Single Leading Underscore (_single_leading_underscore)
'''
-> A variable or method with a single leading underscore is intended for internal use only and is not part of the public API.
-> It acts as a naming convention and does not enforce privacy. Other code can still access the variable or method.
Examples:'''

class Example:
    def __init__(self):
        self._internal_variable = 42  # Meant for internal use

    def _internal_method(self):
        return "Internal Method"

obj = Example()
print(obj._internal_variable)  # Accessible but not recommended

# 6. Double Leading Underscore (__double_leading_underscore)
'''
-> A variable or method with double leading underscores triggers name mangling in Python.
-> The interpreter changes the name of the variable to include the class name as a prefix, making it harder to override or 
   access accidentally from subclasses.
-> The variable __private_variable in a class Example is internally renamed to _Example__private_variable.
-> This prevents accidental access or overrides in subclasses but does not make the variable truly private.
Examples:'''

class Example:
    def __init__(self):
        self.__private_variable = 42  # Name mangled to _Example__private_variable

obj = Example()
# print(obj.__private_variable)  # AttributeError
print(obj._Example__private_variable)  # Access via mangled name

# 7. Double Underscore at Both Ends (variable)
'''
-> Variables or methods with double underscores at both ends are reserved for Python's internal use.
-> These are known as dunder methods (short for "double underscore") or magic methods.
-> You should not create your own identifiers with double underscores on both ends.

Common magic methods:
__init__: Constructor for initializing objects.
__str__: Defines the string representation of an object.
__add__: Defines behavior for the + operator.
__len__: Called by the len() function.
Example:'''

class Example:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Example with value {self.value}"

obj = Example(10)
print(obj)  # Output: Example with value 10

# Good Practices for Naming Identifiers

# 1. General Naming Rules
'''
-> Be Descriptive: Use meaningful names that clearly indicate the purpose of the variable, function, or class.
-> Use Alphanumeric Characters and Underscores Only: Identifiers must start with a letter or an underscore and can contain letters, numbers, or underscores.
-> Avoid Reserved Words: Do not use Python keywords (e.g., if, class, def) as identifiers.'''

# 2. Variable Naming
'''
-> Snake Case for Variables: Use lowercase letters with words separated by underscores.
-> Avoid Single-Letter Names (unless in small loops like i, j):'''

# 3. Function Naming
'''
-> Snake Case for Functions: Use lowercase letters with underscores to separate words.
-> Use Verbs for Action Functions: Start with a verb to indicate the function's purpose.'''

# 4. Class Naming
'''
-> PascalCase for Classes: Capitalize the first letter of each word without underscores.
-> Avoid Prefixing Classes with Abstract Details: Instead of DataHandlerClass, just use DataHandler.'''

# 5. Constant Naming
'''
-> Uppercase for Constants: Use all uppercase letters with underscores to separate words.'''

# 6. Module and Package Naming
'''
-> Lowercase and Short Names: Use short, descriptive lowercase names without special characters.'''

# 7. Avoid Ambiguous or Confusing Names
'''
-> Avoid single underscores (_) for regular variables, as they are used for special purposes (e.g., in the REPL).
-> Avoid names like l, I, or O as they can be confused with 1 or 0.'''

# 8. Prefix or Suffix for Private or Temporary Variables
'''
-> Single Leading Underscore (_variable): Indicates a variable/method is for internal use.
-> Double Leading Underscore (__variable): Triggers name mangling for attributes in classes.
-> Trailing Underscore (variable_): Use to avoid conflict with Python keywords.'''

# 9. Use Consistent Naming Across the Project
'''
-> Stick to one naming convention (e.g., always use snake_case for functions and variables).
-> Follow the same style for similar identifiers across modules.'''

# 10. Real-World Examples

# Good Practice:

# Variable names
customer_name = "John Doe"
max_attempts = 5

# Function names
def calculate_discount(price, discount_rate):
    return price * (1 - discount_rate)

# Class names
class OrderDetails:
    pass

# Constants
DEFAULT_TIMEOUT = 30

# Bad Practice:

# Confusing and inconsistent naming
cn = "John Doe"          # Too short, unclear purpose
MaxAttempts = 5          # Incorrect casing for variables
def calc(price, rate):   # Unclear function purpose
    return price * rate