"""
Set is one of the 4 built-in collection data-types in python.

Sets are UNORDERED, UNCHANGEABLE, UNINDEXED and DUPLICATES NOT ALLOWED.
Set items are unchangeable. But you can remove and add new values
"""

# Sets are definied in using curly brackets, But for defining empty set,
# we have to use set constructor.

my_set = {10, 20}     # Incorrect
# my_set = set()
# print(type(my_set))


# Creating a set with duplicates will not raise an error, but value will only occur once
# x = {"apple", "mango", "apple"}
# print(x)


# Set items are unindexed. Meaning that you cannot use indexes to access it's values
y = {10, 20, 30}
# print(y[2])     # Will raise an error


# We can get set items one by one with a loop
set_1 = {10, 20, "name", False}
# print(set_1)

# for i in set_1:
#     print(i)


# Also you cannot guarentee the order of value appearence in a set since sets are unordered.
# for i in range(20):
#     print(y)

# You cannot change the set values once it is defined
set_2 = {20, 10, 40}
# set_2[1] = 50   # Will raise an error


# Getting the length of a set
# print(len(set_2))


# Set can contain any data types (Except Unhashable types)
# set_3 = {"Harindu", True, None, 10, 50.565, [10, 20]}   # Will raise an error
# print(set_3)


# Can contain tuples because, tuples are hashable
# set_3 = {"Harindu", True, None, 10, 50.565, (12, 78, 89)}
# print(set_3)


# Cannot contain set because, sets are unhashable
# set_3 = {"Harindu", True, None, 10, 50.565, {12, 78, 89}}
# print(set_3)


# Check if an item exists in a set using "in" keyword
# numbers_set = {10, 20, 40, 89, 342}
# print(10 not in numbers_set)



# Set with operators
a = {10, 205}
b = {50, 40}
print(a + b)
