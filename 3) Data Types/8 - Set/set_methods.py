"""
All the methods supported by set data-type
"""


# Add a new value to a set
s = {10, 20, 30}
# s.add(40)
# print(s)



# # Clear the whole set
# s.clear()
# print(s)



# Copy a set (shallow copy)
s2 = s.copy()



# Get the difference of 2 sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# z = x.difference(y)
# print(z)
# k = y.difference(x)
# print(k)



# Removing the items that exists in both sets
# x.difference_update(y)
# print(x)

# y.difference_update(x)
# print(y)



# Removing the specified element from the set.
# Will not raise an error if the item is not found
a = {10, 20, 30}
# a.discard(10)
# print(a)



# Removing the specific element from a set.
# Raises an error if the item not found

a = {10, 20, 30}
# a.remove(10)
# a.remove(656)   # Error
# print(a)



# Returns a set that contains the similarities between 2 or more sets.
# Returns a new set

a = {10, 20, 300, 200}
b = {40, 50, 60, 10, 200}
c = {70, 80, 90,10, 200}
# print(a.intersection(b, c))



# Same as intersection() method. The difference is, intersection_update does not return a new set.
# Instead it removes the items from the original set.

# a.intersection_update(b, c)
# print(a)



# Returns True if none of the items are present in both sets, otherwise False
# a = {10, 20, 300, 200}
# b = {40, 50, 60, 10, 200}
# print(a.isdisjoint(b))



# Check if a subset or not
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}

# print(x.issubset(y))


x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

# print(x.issuperset(y))
# print(y.issuperset(x))



# Removes a random element from a set, and returns the removed element
x = {"f", "e", "d", "c", "b", "a"}
# print(x.pop())



# Return all the items from both sets except the items that present in both sets.
# Return output as a new set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# z = x.symmetric_difference(y)
# print(z)



# Same as the previous one. Difference is this updates the original set
# print(x)
# print(y)
# print("\nAfter modifications\n\n")
# x.symmetric_difference_update(y)
# y.symmetric_difference_update(x)
# print(x)
# print(y)



# Returns a new set containing all the items in all the specified sets.
# Duplicates will be removed

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {10, 20, 50}

# union = x.union(y, z)
# print(union)


# updates a set with another set or any iterable object
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.update(y)
# print(x)