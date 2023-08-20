# 1) FORMATTING WITH % OPERATOR

# about = "String formatting is %s" %'Awesome'
# print(about)

# python = "Python"
# java = "Java"
# languages = "%s and %s are %i popular languages" %(python, java, 2)
# languages = "%s and %s are %.1f popular languages" %(python, java, 2.566787)

# print(languages)



# 2) FORMATTING WITH .format() STRING METHOD

# about = "String formatting {} very {}".format("is", "simple")

# about = "String formatting {1} very {0}".format("is", 'simple')

# about = "String formatting {first} very {second}".format(second='simple', first="is")
# print(about)



# 3) FORMATTING WITH STRING LITERRALS ( f strings )

# name = "Harindu"
# about = f"My name is {name}"

# num_1, num_2, num_3 = 10, 20, 30

# some = f"{num_1 + 30} {num_2} {num_3}"
# print(some)



# 4) Formatting with string template class

# from string import Template

# name = Template("Python is $word")
# formatted = name.substitute(word="Easy")
# print(formatted)
