"""
In python there is a concept called "null", which basically denote a pointer that does
not point to anything or to indicate an empty variable.
In most of the programming languages, null is defined as 0. 

BUT IN PYTHON, THINGS ARE DIFFERENT

In Python, None keyword is used to define null objects and variables.
"""

# init = ''
# print(type(init))

# a = None
# print(type(a))


# if a == None:
#     print("Yes")


# When checking for None, use "is" and "is not".
# Do not use equality operators (==, !=) because it equality operators can be faulty,
# when comparing objects that override the __eq__() method.
# If you must know whether or not you have a None object, then use 'is' and 'is not'.

class MyClass:
    def __eq__(self, *args):
        return True

obj = MyClass()

# print(obj is None)  # Correct
# print(obj == None)  # Faulty


# print([] is None)