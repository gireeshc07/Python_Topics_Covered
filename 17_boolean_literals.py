
# Boolean Literals:
'''
-> The Boolean literal in Python has two values that is either True or False. They are a subclass of integers and play a vital role in decision-making, logical operations, and control flow.
-> It can represent any one of the two values.
    - True represents the numeric value 1
    - False represents the numeric value 0
-> These are immutable, case-sensitive and one of the Python Keywords.
-> First letter should always be in capital, otherwise we get NameError.
'''
# bool() function:
'''
-> Almost any value is evaluated to True if it has some sort of content.
-> Any string is True, except empty strings ("").
-> Any number is True, except 0.
-> Any list, tuple, dict, and set are True, except empty ones.
-> True and 1 are evaluates to True.
-> False, 0 and None evaluates to False.
'''
# e.g., 

print(bool(True))
print(bool(1))
print(bool(1.0))
print(bool(1+2j))
print(bool("Hello"))
print(bool([1,"a"]))
# Output: True

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))
print(bool())
# Output: False

a=True;print(a);print(type(a))

b=False;print(b);print(type(b))

print(True+True, True+False, False+True, False+False)

print(True+4, False+4)

print(True*15, False*15)

print(True/True, )
print(False/True)

# print(True/False)
# print(False/False)

print(int(True),float(True))
print(int(False),float(False))

a=13;a=10;c=a>b;print(c)

print(10>9);print(10==9);print(10<9)

a=200;b=33
if b>a:
    print(True)
else:
    print(False)

def myFunction():
    return True
print(myFunction())

class Myclass():
    def __len__(self):
        return 0
object=Myclass()
print(bool(object))

# -> Python also has many built in functions that return a Boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

# e.g.,

x=200
print(isinstance(x,int))