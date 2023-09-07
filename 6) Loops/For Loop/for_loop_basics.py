"""
For loops are used to iterate over a sequence. Most of the times,
this is used when we know exactly how many iterations are going to happen.

Use For Loop over the while loop, whenever you can, to avoid mistakes and infinite loops.
"""


# For else syntax
# a = 10

# for i in range(a):
#     if i == 3:
#         print("Oops. break found. else clause will not be executed")
#         break
# else:
#     print("Nothing bad happened")


# Just a convention.
# for _ in range(10):
#     print(_)


# Loops can ne nested with each other (loops inside loops)
# for i in range(1, 11):
#     for j in range(10):
#         print(i+j)


# The break keywork breaks or terminates the loop.
# lst = [10, 20, 30, 40, 50]

# for num in lst:
#     if num == 30:
#         break
#     # print(num)
#     # Nothing in here will be executed if the above break statement found.



# The continue statement will continue to the next iteration/round, if found inside a loop body.
for num in range(1, 10):
    if num%2 == 0:
        continue
    print(num)  
    # Nothing in here will be executed if the above break statement found.

