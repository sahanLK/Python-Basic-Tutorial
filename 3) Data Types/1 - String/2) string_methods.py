
# 1) To capitalize a string
# some_string = "python"
# print(some_string.capitalize())



# 2) Convert to lowercase letters (Best suited with unicode characters)
# some_string = "Python is Awesome"
# print(some_string.casefold())



# 3) Convert to lowercase letters (Best suited with ASCII characters)
# some_string = "Python is AwesomE"
# print(some_string.lower())



# 4) Convert to Uppercase letters
# some_string = "Python"
# print(some_string.upper())



# 5) Center align a string with a given length and character
# some_string = "Python"
# print(some_string.center(50, '-'))



"""
6) Count the number of occurences of a given character

USAGE: string.encode()
@params:
    encoding: Optional (default: utf-8)
    errors: Optional
"""
# some_string = "Python is Awesomep"
# print(some_string.count('P'))



# 7) Check if the string ends with the given value or not
# some_string = "Python is Awesome"
# print(some_string.endswith('ehj'))



# 8) Check if the string startswith the given value
some_string = "Python is Awesome"
print(some_string.startswith('Python'))



# 9) Check is all the characters in the string is lowercase or not
# some_string = "Python is Awesome"
# print(some_string.islower())



# 10) Check is all the characters in the string is uppercase or not
# some_string = "Python is Awesome"
# print(some_string.isupper())



# 11) .title()

# To get a title like string. (First character of all the words are uppercase)
# some_string = "python is awesome"
# print(some_string.title())



# 12) .find()
# Find the first occurence of the specified value.
# Returns -1 if the value is not found
# some_string = "pythony is awesome"
# print(some_string.find('R'))



# 13) .index()
# Same as .find(). Only difference is, raises an exception if the value not found
# some_string = "python is awesome"
# print(some_string.index('R'))



# 14) .split()
# Splits the string into a list with a given seperator.
# Default deperator is SPACE

# some_string = "python is awesome"
# print(some_string.split('n'))



# 15) .strip()
# Removes any leading and trailing whitespaces
# Also can specify, which character should be removed

# some_string = "  python is awesome  "
# print(some_string.strip())



# 16) .format()
# Formats the specified values and insert them inside the string's placeholder.
# Placeholder is defined using curly brackets

# some_string = "python is {final}"
# print(some_string.format(final="Awesome"))



# 17) .replace(value_to_be_replaced, new_value)
# Replaces the given value with another given value in a string

# some_string = "Python is Awesome"
# print(some_string.replace('Python', 'Java'))



# 18) .join(sequence)
# Join the given sequence items into a single string with given value

# some_sequence = ["Python", "is", "Awesome"]
# print(" ".join(some_sequence))



# 19) .isspace()
# Check if the string is a space or not

# some_string = "   "
# print(some_string.isspace())



# 20) .istitle()
# Returns True if all words in a text start with a upper case letter, and the rest of the word are lower case letters, otherwise False.

# some_string = "Python is Awesome"
# print(some_string.istitle())



# 21) .splitlines()
# Splits a string at line breaks into a list.

# some_string = """
# Python is a General purpose language,
# and it is easy to learn
# """
# print(some_string.splitlines())



# 22) .swapcase()
# Convert lowercase letters to uppercaseand uppercase letters to lowercase

# some_string = "Python is Awesome"
# print(some_string.swapcase())



# 23) .isdecimal()
# Returns True if all the characters are decimals (0-9). Only accepts decimals

# some_digits = "12345"
# print(some_digits.isdecimal())



# 24) .isdigit()
# Returns true if all the characters are digits. otherwise false. (Accepts decimals, subscripts, and superscripts)

# some_string = "Python is Awesome"
# some_digits = "12345"
# print(some_string.isdigit())



# 25) .isnumeric()
# Similar to isdigit(). But unlke isdigit() and isdecimal(), this method accepts, Subscripts, Superscripts, Roman Numerals, and Currency Numerators

# some_digits = "12345"
# print(some_digits.isnumeric())







# expandtabs
# format_map
# isalnum
# isalpha
# isascii
# isidentifier
# isprintable
# ljust
# lstrip
# maketrans
# partition
# removeprefix
# removesuffix
# rfind
# rindex
# rjust
# rpartition
# rsplit
# rstrip
# translate
# zfill
