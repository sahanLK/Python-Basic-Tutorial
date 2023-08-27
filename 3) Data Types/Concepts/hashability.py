# Hashability only happens with immutable objects
# All python objects has a unique hash value


# Immutable objects has a hash value
a = "Sahan"
# print(a.__hash__())


# Even Mutable objects has a hash value when it contains hashable objects.
b = (10, 20, 30)
# print(b.__hash__())


# If Tuple objects contain unhashable objects, it will raise an error
# c = (10, 20, 30)
# print(c.__hash__())


# But for a list, it can contain unhashable objects. But there will be no hash
# a_list = [10, 20]
# print(a_list.__hash__())  # Error
