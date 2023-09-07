# Questions 1

# num = 7
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")



# Questions 2

# fahrenheit = 98.6
# celsius = (fahrenheit - 32) * 5/9
# print(celsius)



# Questions 3

# word = "radar"

# if word == word[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")



# Questions 4
# numbers = [5, 5, 10, 15, 10, 20]
# unique_numbers = list(set(numbers))
# print(unique_numbers)



# Questions 5
# text = "A man a plan a canal Panama"

# cleaned_text = ''.join(text.split()).lower()
# is_palindrome = cleaned_text == cleaned_text[::-1]
# print(is_palindrome)



# Questions 7

# numbers = [14, 27, 5, 32, 18]
# largest = numbers[0]    # 14, 27, 32


# if numbers[1] > largest:    # 27 > 14
#     largest = numbers[1]
# if numbers[2] > largest: # 5 > 27
#     largest = numbers[2]
# if numbers[3] > largest:    # 32 > 27
#     largest = numbers[3]
# if numbers[4] > largest:    #  18 > 32
#     largest = numbers[4]
# print(largest)


# Questions 7
# numbers = [5, 10, 15, 20]
# total = numbers[0] + numbers[1] + numbers[2] + numbers[3]
# print(total)



# Questions 8
# numbers = [5, 5, 10, 15, 10, 20]
# unique_numbers = [numbers[0]]

# if numbers[1] not in unique_numbers:
#     unique_numbers.append(numbers[1])
# if numbers[2] not in unique_numbers:
#     unique_numbers.append(numbers[2])
# if numbers[3] not in unique_numbers:
#     unique_numbers.append(numbers[3])
# if numbers[4] not in unique_numbers:
#     unique_numbers.append(numbers[4])
# print(unique_numbers)



# Questions 9
text = "Python"
t2 = text[5] + text[4] + text[3] + text[2] + text[1] + text[0]
# print(t2)



# Questions 10
text = "A man a plan a canal Panama"
cleaned_text = ''.join(text.split()).lower()
is_palindrome = cleaned_text == cleaned_text[::-1]
# print(is_palindrome)



# Questions 11

# numbers = [14, 27, 5, 32, 18]
# largest = numbers[0]
# second_largest = numbers[1]

# if numbers[1] > largest:
#     largest = numbers[1]
#     second_largest = numbers[0]
# if numbers[2] > largest:
#     second_largest = largest
#     largest = numbers[2]
# elif numbers[2] > second_largest:
#     second_largest = numbers[2]
# if numbers[3] > largest:
#     second_largest = largest
#     largest = numbers[3]
# elif numbers[3] > second_largest:
#     second_largest = numbers[3]
# if numbers[4] > largest:
#     second_largest = largest
#     largest = numbers[4]
# elif numbers[4] > second_largest:
#     second_largest = numbers[4]
# print(second_largest)



# Questions 12

# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# count_1 = numbers.count(1)
# count_2 = numbers.count(2)
# count_3 = numbers.count(3)
# count_4 = numbers.count(4)
# print({1: count_1, 2: count_2, 3: count_3, 4: count_4})



# Questions 13

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# common_elements = []

# if list1[0] in list2:
#     common_elements.append(list1[0])
# if list1[1] in list2:
#     common_elements.append(list1[1])
# if list1[2] in list2:
#     common_elements.append(list1[2])
# if list1[3] in list2:
#     common_elements.append(list1[3])
# if list1[4] in list2:
#     common_elements.append(list1[4])
# print(common_elements)



# Questions 14
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# print(is_leap)



# Questions 15
# num = 12345
# digit_sum = int(num / 10000) + int((num % 10000) / 1000) + int((num % 1000) / 100) + int((num % 100) / 10) + (num % 10)
# print(digit_sum)



# Questions 16
# default_dict = {}
# keys = ['a', 'b', 'c']
# default_value = 0
# for key in keys:
#     default_dict[key] = default_value
# print(default_dict)



# Questions 17
# student_info = {'name': 'John', 'age': 20, 'gender': 'Male'}
# keys = list(student_info.keys())
# values = list(student_info.values())

# print(type(keys))
# print(type(values))



# Questions 18
# grades = {'Alice': 85, 'Bob': 92, 'Eve': 88, 'Charlie': 92}
# student = 'Eve'
# grade = grades.pop(student)
# print(grade)

# if grade is not None:
#     print(f"{student}'s grade: {grade}")
# else:
#     print(f"{student} not found")



# # Question 19 - (Dictionary Unpacking)
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# merged_dict = {**dict1, **dict2}
# print(merged_dict)



# Question 19
# items = {'apple': 2, 'banana': 3, 'cherry': 2}
# are_values_unique = len(set(items.values())) == len(items)
# print(are_values_unique)



# Question 20
# user_roles = {'admin': 'Admin', 'user1': 'User', 'user2': 'User'}
# username = 'Admin'

# if username in user_roles:
#     print(f"Role: {user_roles[username]}")
# else:
#     print("User not found")



# Question 21
# str1 = "listen"
# str2 = "silent"
# is_anagram = sorted(str1) == sorted(str2)
# print(is_anagram)



# Question 22
# sentence = "This is a sample sentence."

# word_count = len(sentence.split())
# print(word_count)


# Question 23
# num1 = 15
# num2 = 25
# num3 = 10

# largest = num1 if num1 > num2 and num1 > num3 else (num2 if num2 > num3 else num3)
# print(largest)



