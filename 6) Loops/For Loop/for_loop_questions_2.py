
# Question 1
# for i in range(1, 11):
#     print(i)


# Question 2
# for i in range(2, 21, 2):
#     print(i)


# Question 3
# sum = 0
# for i in range(1, 20):
#     sum += i
# print(sum)


# Question 4
# my_list = [1, 2, 3, 4, 5]

# for item in my_list:
#     print(item)


# Question 5
# my_string = "Hello, World!"
# for char in my_string:
#     print(char)


# Question 6
# num = 17
# is_prime = True

# for i in range(2, num):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(f"{num} is prime.")
# else:
#     print(f"{num} is not prime.")


# Question 7
# my_dict = {'a': 1, 'b': 2, 'c': 3}

# for key, value in my_dict.items():
#     print(f"Key: {key}, Value: {value}")


# Question 8
# n = 5
# factorial = 1

# for i in range(1, n + 1):
#     factorial *= i
# print(f"The factorial of {n} is {factorial}")


# Question 9
# for i in range(5):
#     for j in range(i + 1):
#         print("*", end="")
#     print()


# Question 10
# my_list = [10, 45, 32, 78, 5, 97, 62]
# max_value = my_list[0]
# for num in my_list:
#     if num > max_value:
#         max_value = num
# print(f"The maximum value is {max_value}")


# Question 11
# my_list = [1, 2, 3, 4, 5]
# reversed_list = []

# for i in range(len(my_list) - 1, -1, -1):
#     reversed_list.append(my_list[i])
# print(reversed_list)


# Question 12
# my_string = "racecar"
# is_palindrome = True

# for i in range(len(my_string) // 2):
#     if my_string[i] != my_string[-(i + 1)]:
#         is_palindrome = False
#         break
# if is_palindrome:
#     print("It's a palindrome!")
# else:
#     print("It's not a palindrome.")


# Question 13
# n = 10
# fib_sequence = [0, 1]

# for i in range(2, n):
#     next_fib = fib_sequence[-1] + fib_sequence[-2]
#     fib_sequence.append(next_fib)
# print(fib_sequence)


# Question 14
# for num in range(2, 101):
#     is_prime = True

#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=", ")


# Question 15
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# common_elements = []

# for item1 in list1:
#     for item2 in list2:
#         if item1 == item2:
#             common_elements.append(item1)
# print(common_elements)


# Question 16
# my_list = [5, 2, 9, 1, 5, 6]

# for i in range(len(my_list)):
#     for j in range(len(my_list) - 1):
#         if my_list[j] > my_list[j + 1]:
#             my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
# print(my_list)


# Question 17
# base = 2
# exponent = 5
# result = 1

# for i in range(exponent):
#     result *= base
# print(f"{base} raised to the power {exponent} is {result}")


# Question 18
# rows = 5
# for i in range(rows):
#     num = 1
#     for j in range(1, rows - i):
#         print("  ", end="")
#     for k in range(0, i + 1):
#         print(f"{num:2}  ", end="")
#         num = num * (i - k) // (k + 1)
#     print()


# Question 19
# sum_primes = 0
# for num in range(2, 101):
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         sum_primes += num
# print(f"The sum of prime numbers between 1 and 100 is {sum_primes}")


# Question 20
# n = 5

# for i in range(1, n + 1):
#     factorial = 1
#     j = i

#     print(factorial + j)


# Question 21
# n = 36
# p = []
# i = 2

# for num in range(12):
#     if n % i == 0:
#         p.append(i)
#         n = n // i
#     else:
#         i += 1
# print(p)


# Question 22
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transpose = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         transpose[j][i] = matrix[i][j]
# print(transpose)


# Question 23
# d1 = {1: 'Num 1', 2: 'Num 2'}

# for k in d1:
#     for i in d1[k]:
#         print(i)


# Question 24
# s2 = {}

# for string in ['s1', 's2', 's3']:
#     rev = string[1] + string[0]
#     s2[string] = rev
# print(s2)


# Question 25
# d = {1: 100, 2: 200, 3: 300}
# print(type(d))

# for key, val in d.items():
#     for s in str(val):
#         out = int(val) + key
#         print(out)


# Question 26
# Question 27
# Question 28
# Question 29
# Question 30
# Question 31
# Question 32
# Question 33
# Question 34
# Question 35
# Question 36
# Question 37
# Question 38
# Question 39
# Question 40
# Question 41
# Question 42
# Question 43
# Question 44
# Question 45
# Question 46
# Question 47
# Question 48
# Question 49
# Question 50

