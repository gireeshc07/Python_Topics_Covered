
# Sequence and Non-Sequence Types:
'''
-> In Python, data types can be broadly categorized into sequence types and non-sequence types based on whether they maintain an order of elements and allow indexed access.
'''
# 1. Sequence Types:
'''
-> Sequence types store elements in a specific order, allowing access to elements using their position (index).
'''
# Key Characteristics:
'''
-> Elements are ordered.
-> Support indexing and slicing.
-> Can be iterated over using loops like for.
-> Allow operations like concatenation and repetition.
'''
# Examples of Sequence Types:

# 1. Strings (str)
# 2. Lists (list)
# 3. Tuples (tuple)
# 4. Range (range)
# 5. Other Sequence-Like Types:
'''
-> Byte Sequences:
  - bytes: Immutable sequence of bytes.
  - bytearray: Mutable sequence of bytes.
  - memoryview: Provides a view of memory shared by other binary objects (e.g., bytes or bytearray) without copying data.'''
  
# 2. Non-Sequence Types:
'''
-> Non-sequence types do not store elements in a specific order and do not support indexing or slicing.
'''
# Key Characteristics:
'''
-> Elements are unordered (or sometimes ordered but without indexing).
-> Do not support slicing or indexed access.'''

# Examples of Non-Sequence Types:

# 1. Sets (set and frozenset):
'''
-> Unordered collections of unique elements.
-> No indexing or slicing.'''

# 2. Dictionaries (dict):
'''
-> Unordered collections of key-value pairs (ordered since Python 3.7).
-> Access elements by key, not by index.'''
# e.g.,
d = {"a": 1, "b": 2}
print(d["a"])  # Output: 1
     
# 3. Numbers
# 4. Boolean (bool)
# 5. NoneType

# Comparison: Sequence vs Non-Sequence Types
'''
| Feature                  | Sequence Types                      | Non-Sequence Types                 |
|--------------------------|-------------------------------------|------------------------------------|
| Order                    | Ordered                             | Unordered                          |
| Indexing/Slicing         | Supported                           | Not Supported                      |
| Common Operations        | Concatenation, repetition, slicing  | Access by key (e.g., dictionaries) |
| Examples                 | Lists, Strings, Tuples, Range       | Sets, Dictionaries, Numbers        |
'''
# When to Use Which?
'''
-> Use sequence types when the order of elements matters, and you need indexed access or slicing.
-> Use non-sequence types when order is irrelevant, and you want fast membership testing (e.g., with sets) or key-based access (e.g., with dictionaries).
'''
