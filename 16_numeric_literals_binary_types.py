
# Numeric Literals:
'''
-> In Python, there are 3 types of numeric literals:

1. Integer Literals(integer or int)
2. Floating-point Literals
3. Imaginary Literals'''

# 1. Integer Literals:
'''
-> The integer literals are whole numbers with positive or negative, without any decimals, of unlimited length(can be stored in available memory).
-> These integer literals take 28 to 32 bytes of memory.
'''
# e.g.,
a=10
b=35656222554887711
c=-3255522
print(a);print(b);print(c)

import sys
print(sys.getsizeof(a))
print(sys.getsizeof(b))
'''
-> Python supports 4 types of integer literals:
1. Decimal integer literals
2. Binary integer literals
3. Octal integer literals
4. Hexadecimal integer literals'''

# 1. Decimal Integer Literals:
'''
-> It is used in day-to-day life.
-> Any number in between 0-9 we call it as a decimal number.
'''
# e.g.,
a=1234
print(a)

# 2. Binary Integer Literals:
'''
-> A binary integer literal consists of digits 0 and 1 prefixed with "0b or 0B".
'''
# e.g.,
a=0b11011
print(a)

# 3. Octal Integer Literals:
'''
-> An octal integer literal consists of any number in b/w 0 to 7 and prefixed with "0o or 0O".
'''
# e.g.,
a=0o210
print(a)

# 4. Hexa-Decimal Integer Literals:
'''
-> A hexa-decimal integer literal consists of any combination of the digits 0 to 9 and the letters A to F(a to f) and  prefixed with "0x or 0X".
'''
# e.g.,
a=0x12c
print(a)

# 2. Floating Point Literals:
'''
-> The Floating-Point Literals are numbers with positive or negative containing one or more decimals.
-> It can contain a decimal point or an exponent or both, it can take up to 24 bytes of memory.
'''
# e.g.,
a=12.34;print(a)

a=.27;print(a)

a=0.1+0.1+0.1
print(a)
print(a==0.3)

a=round(a,1)
print(a)
print(a==0.3)

# -> We can express floating point numbers with exponential notation or scientific notation.

# The format is: mantissa e or E exponent

# -> These are very useful when we want to represent large values.

# e.g.,

print(1.5e2)
print(1.5e-3)

# 3. Imaginary Literals:
'''
-> Imaginary number is a real number multiplied by the square root of -1(√-1).
-> It can be written in the form of z=bj or bJ.
-> Imaginary literals in Python are complex numbers.
-> Complex numbers are a combination of a real and an imaginary number.
-> It can be written in the form of z=a+bj.
-> Both "a&b" are real numbers but "a" is in the real part and "b" is in the imaginary part.
-> These are mostly used in scientific calculations or mathematical modeling.
'''
# e.g.,
z=9+7j
print(z)

a=1.2+3.7j
print(a)

print(a.real)
print(a.imag)

z = 3 + 4j
print(z.real)  # Output: 3.0
print(z.imag)  # Output: 4.0

# Binary Types in Python:
'''
-> Binary types in Python are used to represent and manipulate binary data. These types are crucial when dealing with raw data such as images, files, 
   or network packets.
-> In Python, binary types usually refer to:
   - Binary literals: 0b prefix for representing binary numbers (e.g., 0b101).
   - Byte sequences: bytes, bytearray, and memoryview are used to represent data in binary form.'''

# Characteristics of Binary Types:
'''
-> bytes: Immutable sequence of bytes (similar to a string but for binary data). Once created, its content cannot be modified.                                  
-> bytearray: Mutable sequence of bytes. Can be modified after creation.                                              
-> memoryview: Provides a view of memory shared by other binary objects (e.g., bytes or bytearray) without copying data. It is mutable if the original 
   object it is refering is mutable (e.g., bytearray), but it is immutable if the underlying object is immutable (e.g., bytes).
'''
# Examples of Binary Types:

# 1. bytes (Immutable):
b = bytes([65, 66, 67])  # Represents binary data for 'A', 'B', 'C'
print(b)  
# Output: b'ABC'

# 2. bytearray (Mutable):
ba = bytearray([65, 66, 67])
ba[0] = 68  # Modify the first byte
print(ba)  
# Output: bytearray(b'DBC')

# 3. memoryview:
b = bytearray([1, 2, 3, 4])
mv = memoryview(b)
print(mv[1])  
# Output: 2
mv[1] = 99    # Modify the underlying data
print(b)      
# Output: bytearray(b'\x01c\x03\x04')
