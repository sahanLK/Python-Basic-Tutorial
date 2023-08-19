# Python String Data type

name = 'Some Name &*(^)/^%@!.'

# String Concatenation
first_name = "First "
last_name = "Last"
print(first_name + last_name)

# Convert a string to uppercase
uppercase_name = name.upper()

# Convert a string to lowercase
lower_name = name.lower()

# Capitalize a string
capitalize_name = name.capitalize()

# Count a value
no_of_times = name.count('e')

# Find the index of a string character
# In python, space is also considerd as a character
position = name.find(' ')

# Check if the string is alphanumeric
is_alpha = name.isalnum()

# Check if all the string characters are alphebetical
alpha = name.isalpha()

# Check is all the characters in a string are spaces or not
is_spaces = name.isspace()

# Check if all the characters are lowercase or not
is_lower = name.islower()

# Check if all the letters are upprcase
is_upper = name.isupper()

print(is_upper)