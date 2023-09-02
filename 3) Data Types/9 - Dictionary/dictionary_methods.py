"""
All the methods supported by Python Dictionary.
"""


# .clear() - Removes all the items from a dictionary

# d = {1: 20, 2: 855, 3: 78845, 'name': 'Harindu'}
# d.clear()
# print(d)


# .copy() - Returns a copy of a dictionary
# d = {1: 20, 2: 855, 3: 78845, 'name': 'Harindu'}
# d2 = d.copy()

# print(id(d))
# print(id(d2))


# .fromkeys(keys, values) - Creates a dictionary with specified keys and values
# keys are required. values are Optional. defalut value is None

# keys = ['name', 'age']
# value = ['Harindu', 25]

# person = dict.fromkeys(keys, value)
# print(person)



# .get() - Returns the value of the specified key

# person = {'name': 'Donny', 'age': 25}
# name = person.get('name')
# age = person.get('age')

# nothing = person.get('invalid_key')

# print(name, age)
# print(nothing)



# .items() - Returns a list that contains all the items as tuples. Very useful when looping a dictionary.
numbers = {
    'odd': [1, 3, 5, 7, 9],
    'even': [0, 2, 4, 6, 8]
}

# items = numbers.items()
# print(items[1]) # Error


# .keys()     -  Retuns a list of keys.
# keys = numbers.keys()
# print(type(keys))



# .values() - Returns a list of values in a dictionary
# values = numbers.values()
# print(values)



# .pop() - Removes an element with the specified key
numbers = {
    'odd': [1, 3, 5, 7, 9],
    'even': [0, 2, 4, 6, 8]
}
# numbers.pop()
# print(numbers)



# .popitem()    - Removes the last inserted item
# numbers.popitem()
# print(numbers)


# .setdefault() - Returns the value of the specified key. If the value doesn't exists, insert the new key with specified value
# numbers.setdefault('even', [-10, -20, -82])
# print(numbers)



# .update() - Updates the dictionary with the specified key-value pairs

