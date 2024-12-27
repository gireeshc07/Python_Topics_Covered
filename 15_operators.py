
# Operators in Python:

# Operators:
'''
-> Operators in Python are symbols or keywords used to perform specific operations on values or variables. 
-> These operations include mathematical calculations, comparisons, logical decisions, bitwise manipulations, and more. 
'''
# Operands:
'''
-> Operands are the values or variables upon which operators perform actions. 
-> In Python, operands can be constants, variables, or expressions.
'''
# Types of Operators:

# In Python, operators can be classified as binary and unary based on the number of operands they work with.

# 1. Binary Operators:
'''
-> Binary operators are operators that operate on two operands. 
-> In Python, binary operators are commonly used to perform arithmetic, comparison, logical, and bitwise operations between two values.
'''
# 2. Unary Operators:
'''
-> Unary operators are operators that operate on a single operand. 
-> These are used for tasks such as negation, bitwise inversion, and Boolean logic inversion.
'''
# Types of Unary Operators:

# 1. Unary Plus (+)
'''
- Definition: Returns the operand's value as is, without any changes.
- Purpose: Often used for clarity or consistency in code, especially in mathematical expressions.
- Behavior: Does not alter the operand; +x is equivalent to x.
'''
# e.g.,
x = 5
print(+x)  # Output: 5

# 2. Unary Minus (-)
'''
- Definition: Negates the operand’s value.
- Purpose: Converts positive numbers to negative and vice versa.
- Behavior: Flips the sign of the operand.
'''
# e.g.,
x = 5
print(-x)  # Output: -5

# 3. Logical NOT (not)
'''
- Definition: Inverts the Boolean value of the operand.
- Purpose: Used in logical conditions to reverse True/False values.
- Behavior:
  - If the operand is True, the result is False.
  - If the operand is False, the result is True.
'''
# e.g.,
is_valid = True
print(not is_valid)  # Output: False

# 4. Bitwise NOT (~)
'''
- Definition: Inverts all bits of the operand.
- Purpose: Performs a bitwise complement, flipping all bits in the binary representation.
- Formula: Result=−(Operand+1) (Two's complement representation).
- Behavior: Converts a positive integer to its two’s complement negative counterpart and vice versa.
'''
# e.g.,
x = 5  # Binary: 00000101
print(~x)  # Output: -6 (Binary: 11111010 in two's complement)

# Types of Operators:

# 1. Arithmetic Operators:
'''
-> It performs a mathematical operation on two numerical operands.'''

# Types of Arithmetic Operators:

# a. Addition(+):

a=10;b=20;c=a+b;print(c)
a=10;b=20.5;c=a+b;print(c)
a=10.5;b=20.5;c=a+b;print(c)
a=10+1j;b=20+2j;c=a+b;print(c)

# b. Subtraction(-):

a=20;b=10;c=a//b;print(c)
a=20;b=10.5;c=a//b;print(c)
a=20.5;b=10.5;c=a//b;print(c)

# c. Multiplication(*):

a=10;b=5;c=a*b;print(c)

# d. Division(/):

a=10;b=5;c=a/b;print(c)

# e. Floor Division(//):

a=20;b=10;c=a//b;print(c)
a=20;b=10.5;c=a//b;print(c)
a=20.5;b=10.5;c=a//b;print(c)

# f. Modulus(%):

a=10;b=5;c=a%b;print(c)

# g. Exponentiation(**):

a=2;b=3;c=a**b;print(c)

# 2. Assignment Operators:
'''
-> It evaluates the right operand which can be values, variables, or expressions and assigns or reassigns the value or result to the left operand.'''

# Types of Assignment Operators:

# a. Assign Operator(=):

a=10;b=10;print(a,b)

# b. Add and Assign Operator(+=):

a=10;b=20;a+=b;print(a,b)
a=10;b=20;c=30;a+=b+c;print(a,b,c)

# c. Subtract and Assign Operator(-=):

a=10;b=20;c=0;print(a,b,c)
a=10;b=20;c=0;a-=b;c-=a+b;print(a,b,c)

# d. Multiply and Assign Operator(*=):

a=3;b=5;a*=b;print(a)

# e. Divide and Assign Operator(/=):

a=3;b=5;a/=b;print(a)

# f. Modulus and Assign Operator(%=):

a=3;b=5;a/=b;print(a)

# g. Floor Divide and Assign Operator(//=):

a=3;b=5;a//=b;print(a)

# h. Exponent and Assign Operator(**=):

a=3;b=5;a**=b;print(a)

# i. Bitwise AND and Assign Operator(&=):

a=3;b=5;a&=b;print(a)

# j. Bitwise OR and Assign Operator(|=):

a=3;b=5;a|=b;print(a)

# k. Bitwise XOR and Assign Operator(^=):

a=3;b=5;a^=b;print(a)

# l. Bitwise Right Shift and Assign Operator(>>=):

a=3;b=5;a>>=b;print(a)

# m. Bitwise Left Shift and Assign Operator(<<=):

a=3;b=5;a<<=b;print(a)

# n. Walrus Operator(:=):

'''
-> It is introduced in Python 3.8.
-> It assigns the value of an expression to a variable and returns the value of an expression.'''

# Syntax => variable := value or expression

a=3;print(a)
# print(a=3) # it raises the TypeError
print(a:=3)

# while(data:=input("enter some date: "))!="exit":
#     print(f'you entered: {data}')

# 3. Comparison or Relational Operators:
'''
-> It is used to compare two values.
-> It returns a Boolean value.
-> It is mostly used in control flow structures.'''

# Types of Comparison Operators:
'''
1. Equals to (==)
2. Not Equals to (!=)
3. Greater than (>)
4. Less than (<)
5. Greater than or Equals to (>=)
6. Less than or Equals to (<=)

e.g. '''

a=10;b=10;print(a==b);print(a!=b)

a=10;b=10;c=a==b;d=a!=b;print(c,d)

a=10;b=10;print(a>b,a<b,a>=b,a<=b)

a=[20,30];b=[20,30];print(a==b,a>b,a<b,a>=b,a<=b)

a=[20,30,"hii"];b=[20,30];print(a==b,a!=b,a>b,a<b,a>=b,a<=b)

a="hii";b="hello";print(a==b)

a={"a":1,"b":2}
b={"a":1,"b":2}
print(a==b)

# 4. Identity Operators:
'''
-> It is used to compare the memory locations of the two objects.
-> It only compares whether two objects are sharing same memory location or not but it does compare whether two objects are having same content 
   or not.
-> It has only two types, they are:

1. is --> If two objects are sharing same location it returns True, if not it returns False.

2. is not --> If two objects are not sharing same location it returns True, if not it returns False.

e.g. '''

a=["apple","banana"]
b=["apple","banana"]
print(a is b)
c=a
print(a is c)
print(a==b)
print(a==c)

print(a is not b)
print(a is not c)
print(a!=b)
print(a!=c)

# 5. Membership Operators:
'''
-> It checks whether specified value is present in the sequence or not.
-> We can give any iterable object as a sequency.
-> It has only two types, they are:

1. in --> If the specified value is present in the sequence, it returns True if not it returns False.

2. not in --> If the specified value is not present in the sequence it returns True if not it returns False.

e.g. '''

a="Hello World"
print("Hello" in a);print("H" not in a)

a=[10,20,"Hello World"]
print("Hello" in a);print(10 not in a)

a={"a":"gireesh","b":25}
print(25 in a);print("b" in a)
print("a" in a);print("a" not in a)

# 6. Logical Operators:
'''
-> It combines and evaluates the conditional statements.
-> It returns the Boolean value.
-> It follows the Truth Table.
-> It has three types, they are:'''

# 1. Logical AND(and):
'''
-> It returns True if given two conditions are True or else it returns False.

e.g. '''

x=10
print(x>3 and x>6, x>3 and x<6, x<3 and x>6, x<3 and x<6)
print(True and True, True and False, False and True, False and False)

# Some more rules in Logical AND:
'''
Condition-1          Condition-2         RESULT

True           -     Expression    -     Expression
False          -     Expression    -     False
Expression     -     True          -     True
Expression     -     False         -     False

e.g. '''

a=5
b=10
c=100
print(a<b and c);print(c and a<b);print(a<b and c and b)

print(a>b and c);print(c and a>b);print(a>b and c and b)


# Finding the maximum number among 3 values:

# e.g.
 
a=10
b=15
c=20
print(a>b and a>c)
print(b>a and b>c)
print(c>a and c>b)

# 2. Logical OR(or):
'''
-> It returns True if any one of the conditions is True, if not it returns False.

e.g. '''

x=10
print(x>3 or x>6, x>3 or x<6, x<3 or x>6, x<3 or x<6)
print(True or True, True or False, False or True, False or False)

# Some more rules in Logical OR:
'''
Condition-1          Condition-2         RESULT

True           -     Expression    -     True
False          -     Expression    -     Expression
Expression     -     True          -     Expression
Expression     -     False         -     Expression

e.g. '''

a=5
b=10
c=100
print(a<b or c);print(c or a<b);print(a<b or c or b)

print(a>b or c);print(c or a>b);print(a>b or c or b)

# 3. Logical NOT(not):
'''
-> It inverts the result.
    True  ---> False
    False ---> True
    
e.g. '''

a=True
b=False
print(a, b);print(not a, not b)

a=10
b=20
print(not(a<b and b>a))

# AND, OR, NOT

a=(15>10) and (10<11) or (7>6) and (15<10)
print(a)
print(not a)

# 7. Bitwise Operators:
'''
-> It is used to perform bitwise calculations on integers.
-> It is also used to compare binary numbers.
-> Computers store all kinds of information as a stream of binary digits called bits.
-> Whether you are working with text, images, or videos, they all boil down to ones and zeros.
-> Python's bitwise operators let you manipulate those individual bits of data at the most granular level.

Decimal Numbers --> Binary Numbers --> Bitwise performed on each bit --> result is returned in Decimal Format'''

# Types of Binary Operators:

# 1. Bitwise AND operator(&):

# e.g.

a=12
b=13
c=a&b
print(c)
print(bin(12))

# 2. Bitwise OR(|):

# e.g.

a=12
b=13
c=a|b
print(c)
print(bin(13))

# 3. Bitwise XOR(^):

# e.g.
 
a=20
b=4
c=a^b
print(c)
print(bin(16))

# 4. Bitwise NOT(~):
'''
-> It is an unary operator because it can be performed on only one operand.
-> It always returns the 2's complement of the value.
-> Alternative names for Bitwise NOT:
    # 1's complement
    # NOT operator
    # Negation

e.g. '''

a=12
print(~a)

print(~20)

# ~x = ~x - 1 --> using this formula we can get the Bitwise NOT of a number by hand

# 5. Bitwise Left Shift(<<):

# syntax : value << no. of shifts

# e.g.

a=10
print(a<<2)

# 6. Bitwise right Shift(>>):

# syntax : value >> no. of shifts

# e.g.

a=10
print(a>>2)

# Order Precedence:
'''
-> It describes the order in which operations are performed.
-> Order precedence is mostly used when we have an expression with more than one operator.
-> In mathematics, we have the BODMAS rule, but in Python, we have the order of precedence.'''

# Order of order precedence in Python:
'''
1. Parentheses ()
2. Exponentiation **
3. Unary Plus(+a), Unary Minus(-a), Bitwise NOT(~a)
4. Multiplication(*), Division(/), Floor Division(//), Modulus(%)
5. Addition(+), Subtraction(-)
6. Bitwise Left Shift(<<), Bitwise Right Shift(>>)
7. Bitwise AND(&)
8. Bitwise XOR(^)
9. Bitwise OR(|)
10. Comparison, Identity, Membership Operators
11. Logical NOT(not)
12. Logical AND(and)
13. Logical OR(or)

Note: If two operators have the same precedence, the expression is evaluated from left to right.

e.g. '''

print(5+4-7+3)
print((5+4)-(7+3))

print(100+5*3)
print((100+5)*3)

print(6*3+4**2//5-8)

print(3<5 or 50/(5-(3+2)))

# print(50/(5-(3+2)) or 3<5) # ZeroDivisionError occurs
