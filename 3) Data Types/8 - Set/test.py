


"""
Requirements
None - It is a None value
string - it is a string
list = I
"""

# n = None
# print(type(n))

lst = [None, "SAhan", False, ["45", None], True]

for item in lst:
    if isinstance(item, type(None)):
        print("It is a None value")
    elif isinstance(item, str):
        print("It is a string")
    elif isinstance(item, bool):
        print("It is a boolean")
    elif isinstance(item, list):
        print("It is a list")
    else:
        print("Unidentified type")
