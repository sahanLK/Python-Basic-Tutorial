"""
Python Lists

Lists are created using square brackets
List items are Ordered, Changeable and Allow duplicate values.
"""


# Accessing items with index
lst = ['item_1', 20, 50, None, True, [10, 20, 30]]
# print(lst[5][2])


# Negative indexing is also possible
# print(lst[-2])


# Range of indexes can also be taken
# print(lst[1:3])
# print(lst[-80:-1])  # Will not raise an error


# Check if an item exists in the list
# print(500 in lst)


# Change list items
orig = [0, 2, 4, 6, 8]
# orig[1] = 500
# print(orig)

# When changing, new value doesn't have to be in existing value's data type
orig[4] = None
# print(orig)

# Changing a range of list values
lst = ['item_1', 20, 50, None]
# print(orig)
# orig[2:5] = ['new', '']
# print(orig)

# When inserting more values than index range, new items will be added accordingly
numbers = [100, 200, 300, 400, 500]
# numbers[1:2] = [250, 270, 290]
# print(numbers)

# When inserting more values than index range, new items will be added accordingly
# numbers[1:4] = [2500]
# print(numbers)


# Getting the length of a list
# print(len(lst))


# Creating a list with "list" constructor
# lst = list("Some String")
# print(lst)

# lst_2 = list((10, 20, 30))
# print(type(lst_2))


# Deleting a list item
lst = [10, 20, 30]
# del lst[1]
# print(lst)


# Deleting the whole list
# del lst
# print(lst)


# Joining lists
# l1 = [10, 20, 30]
# l2 = [40, 50, 60]

# print(l2 + l1)


# Joining using loops

# for item in l2:
#     l1.append(item)

# print(l1)
