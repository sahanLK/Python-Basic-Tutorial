
# Creating a Dictionary with curly brackets
# d = {}


# Creating an empty dictionary with dictionary constructor
# d2 = dict()
# print(type(d2))

# d2 = dict(num_1 = 10, num_2 = 20, num_3 = 30)
# print(d2)


# Creating a dictionary with items
#  Duplicate keys will not raise an error, but will overwrite existing values.
car = {'brand': 'Volvo', 'color': 'Black', 'brand': 'BMW'}
# print(car)

"""
In above car dictionary,
    1) brand, color - are considered as keys. (Each item has a unique key)
    2) Volvo, Black - are considered as values

    Key and the value are separated from each other with a colon.
    Values are separated with a comma.
"""


# Getting the length of a dictionary
a = {'num_1': 10, 'num_2': 20, 'num': 30}
# print(len(a))


# Dictionary key is a unique identifier in the dictionary, It could be any hashable object.
d = {
    'str_key': 'String Key Value',
    10: 'Integer Key Value',
    # [10, 20]: 'List Key Value',   # Will generate an error
    # {'a': 10, 'b': 20}: 'Dictionary as a key',    # Will generate an error
    # {10, 20}: "",   # Will generate an error
    (10, 20): 'A Tuple as a Key'
    }


# Accessing dictionary values with key. If the key not found, an error will be raised.
# print(d['str_key'])
# print(d[1])   # Index access is not posiible


# Accessing values with .get() method. If the key not found, NO error will be raised.
# print(d.get(1565))



# Since dictionaries doesn't allow duplicates, dictionary cannot have 2 items with the same key.
# d3 = {'key': 10, 'key': 105}
# print(d3)
# print(d3['key'])


# The values in a dictionary can be of any data type
# d4 = {1: 'A string', 2: [10, 20], 3: (40, 23), 4: {'a': 56}, 5: {10, 50}}
# print(d4[4]['a'])



# Changing dictionary values. # If the item does not exist, new item will be added
d = {1: 10, 2: 20}
# d['1'] = 500

# print(d)



# Also can use the update() method. The argument must be another dictionary.
# If the item does not exist, new item will be added

# d = {1: 10, 2: 20}
# d.update({3: 50, 4: 5645})
# print(d)



# Nested Dictionaries (Dictionary can contain other dictionaries).

school = {
    'class_1': {
        'stu_1': {'name': 'Hashan', 'age': 25}
    },
    'class_2': {
        'stu_1': {'name': 'Tharindu', 'age': 26}
    },
    'class_3': {
        'stu_1': {'name': 'Harindu', 'age': 35}
    },
}

# Accessing items in netsed dictionaries.
# a = school['class_1']['stu_1']['age']

# print(a)





