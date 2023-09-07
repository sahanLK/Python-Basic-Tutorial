"""
Ternary operators / Short-hand if else

SYNTAX: VAL_IF_TRUE if CONDITION else VALUE_IF_FALSE
"""

a = 10
# print("True" if 10 < 20 else "False")


b = [10, 20, 30]
out = True if len(b) >= 3 else False if 5 > 4 else "No" if True or False else False
print(out)



