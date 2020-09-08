"""
# Hello World

print("Hello world!")

print('*' * 10)

# Variable

price = 10
price = 20
name = 'Mark'
is_changed = True # False

print(price)

# Input

name = input('What is your name? ')
print(f'Hi {name}')

# Type conversion

birth_year = input('Birth year: ')
# print(type(birth_year))
# int()
# float()
# bool()
# str()
age = 2020 - int(birth_year)
print(age)

# String

# course = 'Python for "Beginners"'
course = '''
Hi Mark,

Here is our first email to you

Tks,
Lih
'''

# print(course)
course = 'Python for Beginners'
another = course[:]
print(another)
print(course[0:])
print(course[0])
print(course[0:3])
print(course[:])

# Formatter string

first = 'Mark'
last = 'Nguyen'
msg = f'{first} [{last}] is a coder' 
print(msg)

# Python String
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course)
print(course.find('Python'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course)
print(course.title())

# Arithmetic Operations
# Interger 10
# Float 10.123
# + - * / // % ** 

# Operator Precedence
# level 1: ()
# 2: **
# 3: * /
# 4: - +

# Math Function
import math

x = 2.9
print(round(x))
print(abs(-2.9))

print(math.ceil(2.9))
print(math.floor(2.9))

"""

# If condition
is_hot = False
is_cold = False

if is_hot:
  print("It's a hot day")
  print("Drink plenty of water")
elif is_cold:
  print("It's a cold day")
  print("Wear warn clothes")
else:
  print("It's a lovely day")