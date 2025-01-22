
# Control Flow Statements:
'''
-> The control-flow statements of a language specify the order in which computations are performed.
-> There are mainly three key constructs that are used by every programming language in the execution of a program.
        1. Sequence
        2. Selection and 
        3. Iteration'''

# 1. Sequence:
'''
-> In a sequence construct, the statements in a program are executed in the order in which they appear.
-> Python started executing instructions at the top of the program going down, one after another.
'''
# e.g., 
a=10
b=20
c=a+b
print(c)

# 2. Selection:
'''
-> Selection allows us to choose b/w two or more alternatives. It allows us to make decisions.
-> The basic decision statement in the computer is the two-way selection.
-> The decision is described to the computer as a conditional statement that can be answered either True or False.
-> If the answer is True, one or more action statements are executed.
-> If the answer is False, then a different action or set of actions is executed.
-> Regardless of which set of actions is executed, the program continues with the next statement after the selection.'''

# Types of selection statement:
'''
1. if
2. elif
3. else
4. nested if
5. short-hand if
6. short-hand if else'''

# if :
'''
Syntax:
         if (condition):
               statement 1
               statement 2
'''              
# e.g.,    
x=10
if x>10:
    print("let's go for a movie")
if x<3:
    print("let's go for the ride")
print("program terminated")

# elif:
''' 
-> The elif keyword is Python's way of saying "if the previous conditions were not True, then try this condition.

Syntax:
           if (condition 1):
                statement 1
                statememt 2
           elif(condition 2):
                statement 1
                statememt 2
           elif (condtion 3):
                statement 1
                statememt 2         
'''
# e.g.,
x=1
if x==1:
    print("one")
if x==2:
    print("two")
if x==1:
    print("three")
if x==2:
    print("four")
if x==1:
    print("five")

x=1
if x==1:
    print("one")
elif x==1:
    print("two")
elif x==1:
    print("three")
elif x==1:
    print("four")
elif x==1:
    print("five")

x=1
if x==2:
    print("one")
elif x==1:
    print("two")
elif x==1:
    print("three")
elif x==1:
    print("four")
elif x==1:
    print("five")

# else:
'''
-> The else keyword catches anything which isn't caught by the preceding conditions.

Syntax:
          if (condition):
              statement 1
              statement 2
          else:
              statement 1
              statement 2
'''
# e.g.,
x=5
if x<3:
    print("this is if")
elif x>3:
    print("this is elif")
else:
    print("this is else")
print("program terminated")

x=5
if x<3:
    print("this is if")
elif x>6:
    print("this is elif")
else:
    print("this is else")
print("program terminated")

x=2
if x>3:
    print("let's go for a movie")
else:
    print("let's go for the bike ride")
print("program is terminated")

# Nested if:
'''
-> We can have if statements inside if statements, this is called nested if statements.
'''
# e.g.,
x=40
if x>10:
    print("this is outer if")
    if x>20:
        print("this is inner if")
    else:
        print("this is inner else")
else:
    print("this is outer else")
print("program is terminated")

x=40
if x>10:
    print("this is outer if")
    if x<20:
        print("this is inner if")
    elif x>20:
        print("this is inner elif")
    else:
        print("this is inner else")
elif x<10:
    print("this is outer elif")
else:
    print("this is outer else")
print("program is terminated")

# name=input("enter your name: ")
# if name=="ram":
#     rgno=int(input("enter your rg.no.: "))
#     if rgno==1:
#         marks=450
#         print("your marks: ",marks)
#     else:
#         print("please enter a valid rg.no.")
# else:
#     print("please enter a valid name")
# print("program is terminated")

# Short-Hand if:
'''
-> If you have only one statement to execute, you can put it on the same line as the if statement.
'''
# e.g.,
a=200
b=33
if a>b:print("a is greater than b")

# Short-Hand if-else:
'''
-> If you have only one statement to execute, one for if, and one for else, you can put it all on the same line.
'''
# e.g.,
a=2
b=330
print("small") if a>b else print("big")
'''
-> This technique is known as Ternary Operators, or Conditional Expressions.
-> You can also have multiple else statements on the same line.
'''
# e.g.,
a=330
b=330
print("smaller") if a>b else print("equals") if a==b else print("bigger")

# 3. Iterative Statements:
'''
-> When one or more statements are executed repeatedly, this is known as "looping" or "iteration".
-> In looping, the set of instructions are executed repeatedly until a termination condition is satisfied.
-> A program loop therefore consists of two segments, one known as the body of the loop and the other as the control statement.
-> The control statement tests certain conditions and then directs the repeated execution of the statements contained in the body of the loop.'''

# Loop:
'''
-> to repeat the process
-> In Python we have 2 types of loops, they are:
1. while loop
2. for loop'''

# while loop                          for loop
'''
-> to repeat statements             -> to repeat statements
-> condition based                  -> sequence based
-> till condition fails             -> till sequence ends
-> can't use range()                -> can use range()'''

# 1. while loop:
'''
-> The Python while loop allows a part of the code to be executed until the given condition returns False.
-> It is also known as a pre-tested loop.'''

# Types of while loop:
'''
1. while loop
2. infinite while 
3. while loop with else
4. nested while loop'''

# 1. while loop:
'''
Syntax:

counter variable
while (condition):
    statement 1
    statement 2
    Increment/Decrement operation
'''
# e.g.,
print("Number 0")
print("Number 1")
print("Number 2")
print("Number 3")
print("Number 4")

i=0
while i<5:
    print("Number ",i)
    i=i+1
print("program is terminated")

# Even numbers
i=0
while i<=10:
    print(i)
    i+=2
print("program is terminated")

# Even numbers in reverse
i=10
while i>=0:
    print(i)
    i-=2
print("program is terminated")

# odd numbers
i=1
while i<=11:
    print(i)
    i+=2
print("program is terminated")

# odd numbers in reverse
i=11
while i>=0:
    print(i)
    i-=2
print("program is terminated")

# 2. Infinite while loop:
'''
-> It generates never ending while loop
-> It does not have an increment or decrement statements

Syntax:

counter variable
while (condition):
    statement 1
    statement 2
'''
# e.g.,
# i=1
# while i<=10:
#     print("Number ", i)
# print("program is terminated")

# i=1
# while True:
#     print("Number ",i)
# print("program is terminated")

# 3. while loop with else:
'''
-> With the else statement we can run a block of code once when the condition is no longer True.

Syntax:

counter variable
while (condition):
    statement 1
    I/D statement
else:
    statement 1
'''
# e.g.,
i=1
while i<=5:
    print(i)
    i=i+1
else:
    print(" i am from else block")
print("program is terminated")

# 4. Nested while loop:
'''
-> Declaring a while loop in an existing loop is known as Nested while loop.

Syntax:

counter variable 1
counter variable 2
while (condition 1):
    while (condition 2):
    statements
    I/D 1
    I/D 2
'''
# e.g.,
i=1
j=1
while i<=5:
    while j<=5:
        print(i,j)
        i+=1
        j+=1
print("program is terminated")

# 2. for loop:
'''
-> The for loop is used for iterating over a sequence (any iterable object).
-> First the sequence is checked, then, the first item in the sequence is assigned to the iterating variable until the sequence becomes empty.'''

# Types of for loop:
'''
1. for loop
2. for loop with range()
3. for loop with else
4. nested for loop'''

# 1. for loop:
'''
Syntax:

for iterating variable in sequence:
    statement 1
    statement 2
    statement 3
'''
# e.g.,
for i in "hello":
    print(i)
print("program is terminated")

for i in ["hello",2,2.0]:
    print(i)

list=[10,20,30,40]
sum=0
for i in list:
    sum=sum+i
print("Total value: ",sum)
print("program is terminated")

# 2. for loop with range():
'''
Syntax:

for iterating variable in range():
    statement 1
    statement 2
    statement 3
'''
# e.g.,
for i in range(1,5):
    print(i)
print("program is terminated")

for i in range(0,10,2):
    print(i)
print("program is terminated")

for i in range(0,-10,-2):
    print(i)
print("program is terminated")

a="hello"
for i in range(len(a)):
    print(i)
print("program is terminated")

# 3. for loop with else:
'''
Syntax:

for iterating variable in sequence:
    statement 1
else:
    statement 1
'''
# e.g.,
for i in range(0,5):
    print(i)
else:
    print("i am from else block")
print("program is terminated")

for i in range(0,6):
    if i%2==0:
        print(i," is even")
    else:
        print(i," is odd")
print("program is terminated")

# 4. Nested for loop:
'''
-> for loop inside a for loop.

Syntax:

for iterating_variable in sequence:
    statement 1
    for iterating_variable in sequence:
        statement 2
'''
# e.g.,
list=["apple","banana"]
for i in range(1,3):
    print("outer loop: ",i)
    for i in list:
        print("inner loop: ",i)
print("program is terminated")

adj=["red","green"]
frt=["apple","banana"]
for i in adj:
    for j in frt:
        print(i,j)
print("program is terminated")

# for i in range(1,1001):
#     for j in range(1,11):
#         print(i*j,end=" ")
#     print()
# print("program is terminated")

# Unconditional Jumping Statements:

# 1. Break:
'''
-> The break is a keyword in Python which is used to bring the program control out of the loop. The break statement breaks the loop one by one i.e., in the case of nested loops, it breaks the inner loop first and then proceeds to outer loops.

Syntax:

while (condition):                for i in sequence:
    if (condition):                   if (condition):
        break                             break
'''
# e.g.,
# break in while loop
i=0
while i<=10:
    print(i)
    if i==4:
        break
    i+=1
print("program is terminated")

i=0
while i<=10:
    if i==4:
        break
    else:
        print(i)
        i+=1
else:
    print("program is terminated")

# break in for loop
for i in range(10):
    print(i)
    if i==4:
        break
print("program is terminated")

for i in range(10):
    if i==4:
        break
    else:
        print(i)
else:
    print("program is terminated")

# break in nested loops
i=1
while True:
    print("outer loop")
    while True:
        if i>5:
            break
        else:
            print("inner loop ",i)
        i=i+1
    break
print("program is terminated")

for i in range(1,3):
    for j in range(1,4):
        print(i,j)
print("program is terminated")

for i in range(1,3):
    for j in range(1,4):
        if j==3:
            break
        else:
            print(i,j)
print("program is terminated")

for i in range(1,3):
    for j in range(1,4):
        if j==3:
            break
        else:
            print(i,j)
    break
print("program is terminated")

# 2. Continue:
'''
-> The continue statement in Python is used to bring the program control to the beginning of the loop.
-> It stops the current iteration of the loop and continues with the next iteration.
'''
# e.g.,
i=0
while i<4:
    i+=1
    if i==3:
        continue
    print(i)
print("program is terminated")

for i in range(5):
    if i==3:
        continue
    print(i)
print("program is terminated")

for i in range(1,5):
    if i%2==0:
        continue
    else:
        print(i)
print("program is terminated")

for i in "hello":
    if i=="e":
        continue
    else:
        print(i)
print("program is terminated")

fruits=["apple","banana","cherry"]
for i in fruits:
    if i=="banana":
        continue
    else:
        print(i)
print("program is terminated")

# 3. Pass:
'''
-> The pass statement is used as a placeholder for future code.
-> When the pass statement is executed, nothing happens, but you avoid getting an error when an empty code is not allowed.
-> Empty code is not allowed in loops, function definitions, class definitions, or in if statements.

Syntax:

if (condition):               while (condition):           for i in sequence:
    pass                          pass                           pass


if (condition):               counter variable             for i in sequence:
    pass                      while (condition):               if (condition):
else:                             if (condition):                  pass
    statement 1                       pass                      else: 
                                  else:                            statement 1
                                      statement 1
'''
# e.g.,
if 5>2:
    pass

if 5>2:
    pass
else:
    print("i am from else block")

i=0
while i<=10:
    if i>4:
        pass
    else:
        i+=2
        print(i)

for i in range(5):
    if i>3:
        pass
    else:
        print(i)

i=0
while i==0:
    pass

for i in range(5):
    pass