# This concept only applies to compound objects (objects that contain other objects).
# import copy


li1 = [1, 2, [3, 5], 4]

# li2 = copy.copy(li1)
li2 = li1.copy()

# using deepcopy to deep copy
# li2 = copy.deepcopy(li1)

print(li1)

li2[2][1] = 7

print(li2)

print(li1)
