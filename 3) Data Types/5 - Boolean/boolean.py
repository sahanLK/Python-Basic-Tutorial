"""
Booleans are useful to know if an expression is True or False in Programming.
When we compare 2 values, the expression returns either True or False after evaluation.

In python Boolean data type is called as 'bool' and only True or False values can have that data type.
"""

# print(10 > 98)
# print(14 == 8)
# print(10 < 9)


# When evaluating a condition, it also returns either True or False
x = 200
y = 33

# if y > x:
#   print("y is greater than x")
# else:
#   print("y is less than x")



# Python bool() function allows to evaluate any value, and returns either True or False
# print(bool("Hello"))
# print(bool(15))
# print(bool([10, 20, 30, 5]))


# Even though most of the values are evaluated to True, there are some scenarios that we get False, like below.
"""
Empty values (empty list, set, string, dictionary and etc)
None
False itself evaluated to False
Zero
"""

# print(bool(1))
# print(bool(0))
# print(bool(""))
# print(bool([]))
# print(bool(set()))
# print(bool({}))


# Boolean with conditions

# a = 0

# if a:
#     print("a is True")
# else:
#     print("a is False")


# Check if a list is empty or not
lst = []

# if lst:
#     print("List is not empty")
# else:
#     print("List is empty")


a = True

# No need to directly compare the boolean values.
# if a == True:
#     print("It is True")

# Instead just use boolean value
# if a:
#     print("It is True")
