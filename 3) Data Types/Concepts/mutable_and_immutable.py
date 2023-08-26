# Immutable data types does not allow you to change it's internal state and update the value.

num = 7
# print(id(num))


# Below assignment will not going to update the 'num' variable. Instead, it will create
# a completely new value and let your variable refer to it. 
# (It doesn't allow you to change the value stored in original memory address)
num = 10
# print(id(num))


s = {10, 20, 30}
print(id(s))

s.add(50)
print(id(s))