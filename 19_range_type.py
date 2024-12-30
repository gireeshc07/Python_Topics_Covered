
# Range Data Type in Python:
'''
-> In Python, range() is a built-in function that generates an immutable sequence of numbers. We must use this range() funcrion to generate these range of numbers.
-> It creates an immutable object called a range object, which represents a sequence of numbers from a start value to a stop value, with a specific step size. 
-> The range() is associated with its own data type in Python, called the 'range' data type.
-> It is commonly used for looping a specific number of times in "for" loops and other scenarios where a sequence of numbers is required.
'''
# Characteristics of the range Data Type:

# 1. Immutable: Once a range object is created, its values cannot be changed. You must create a new range object for different values.

# 2. Sequence Type: range belongs to Python's sequence types (alongside list, tuple, etc.), which means it supports indexing, slicing, and iteration.
          
# 3. Memory Efficiency:Unlike lists or tuples, a range object does not store all elements in memory. Instead, it calculates values as needed, making it efficient for large ranges.
# e.g.,
large_range = range(0, 10**9)
print(large_range[1000000])  # Efficiently retrieves the millionth number

# 4. Versatility: It can be used for loops, indexing, or slicing without creating a memory-heavy list.

# syntax: range ( Start, Stop, Step )

# 1. Start(inclusive):
'''
-> Optional parameter, default value : 0.
-> It indicates the starting number of the sequence.
'''
# 2. Stop(exclusive):
'''
-> Required parameter, no default value.
-> It indicates the ending number of the sequence.
-> Stop value will not get included in the result, it takes n-1 of the value.
'''
# 3. Step:
'''
-> Optional parameter , default value : 1.
-> It indicates the difference between each number in the sequence or specifies the increment value.
-> The step parameter determines how much to add if positive or subtract if negative to the current number in the sequence to get to the next number but it seems to include one less element than expected, it is due to how the range is defined in Python.
-> The sequence stops generating numbers before it reaches the stop value, hence the feeling of having n-1 elements or steps.
'''
# Points to remember:
'''
-> The range() function only works with integer arguments. Does not allow floating-point steps directly (workarounds are required using libraries like numpy).
-> All three arguments can be positive or negative.
-> The step value cannot be zero.
-> Stop value will not be included in the result.
'''
# e.g.,

a=range(5)
print(a)
# Output: range(0, 5)
print(type(a))
# Output: <class 'range'>

a=range(1,10,2)
print(a)
# Output: range(1, 10, 2)
print(type(a))
# Output: <class 'range'>

a = range(10) 
print(a[2]) # You can access individual elements of a range object using indexing.
# Output: 2
print(a[-1])
# Output: 9

print(len(range(2, 10, 2))) # Use len() to find how many numbers are in the range.
# Output: 4

print(5 in range(10)) # You can check if a number exists in the range using in.
# Output: True
print(15 in range(10))  
# Output: False

# range() function in for loops:

# -----------------------------------------------------------------
#   |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6  7  8  9  10

# If step value is positive, move in forward direction.
# If step value is negative, move in backward direction.

# e.g.,

for x in range(-3,5,-1):
    print(x)

for x in range(6,1):
    print(x)

for x in range(-6,0):
    print(x,end=" ")

for x in range(10):
    print(x,end=" ")
print()

for x in range(3,10):
    print(x,end=" ")
print()

for x in range(0,10,2):
    print(x,end=" ")
print()

for x in range(10,0,-2):
    print(x,end=" ")
print()

for x in range(0,-10,-2):
    print(x,end=" ")
print()

# -> The "range" object is lazy, meaning it generates numbers on demand, which makes it memory efficient.
# -> It can be converted to a list using "list(range(...))" if you need to work with the sequence directly.

# e.g., 
a=range(1,5)
print(list(a))

# -> The "range" function is very useful in scenarios where you need to iterate over a sequence of numbers without the need to create a large list in memory.

# Is range() a Data Type in Python?
'''
-> Yes, range() is associated with its own data type in Python, called the range data type.
-> The range function produces a range object, which is a unique data type in Python. 
-> Recognizing range as a data type helps you leverage its benefits in writing cleaner, more efficient Python programs.
'''
# Is range() a Literal?
'''
-> No, range() is not a literal because it represents a dynamically generated sequence, not a fixed, constant value in the code.
-> It is a function that constructs a range object, which is memory-efficient and immutable.
-> Literals, on the other hand, are directly represented, fixed values like [1, 2, 3] or 'Hello'.
'''
# Is range() a part of built-in data structures in Python?
'''
-> No, range() is not considered a part of built-in data structures in Python. 
-> It is a built-in function that generates an immutable sequence of numbers. 
-> The range() function is typically used in loops (e.g., for loops) to iterate over a sequence of numbers.
-> Although range() produces an iterable sequence, it is not classified as a data structure like lists, tuples, sets, or dictionaries, which store and manage data. 
-> Instead, it represents a sequence of numbers on demand, without storing all values in memory at once, making it memory efficient.
'''
# e.g.,
# Example of using range()
for i in range(5):
    print(i)

# This will output:
0
1
2
3
4
# While it behaves like a sequence, range() itself is not a data structure, but rather an iterable used in iteration and range-based operations.
