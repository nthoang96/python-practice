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

# Logical Operators
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
  print('Eligible for Loan')

# or
# and not

#  Comparison Operators
temperature = 30

if temperature > 30:
  print('Hot')
else:
  print('Not Hot')

# While Loop
i = 1
while i <= 5:
  print(i * '*')
  i += 1
print("Done")

req = ""
isStart = False
while req != 'quit':
  # req = input()
  req = input('> ')
  if req.lower() == 'help':
    print('''
      start - to start the car
      stop - to stop the car
      quit - to exit
    ''')
  elif req.lower() == 'start':
    if isStart:
      print('Car is already started')
    else:
      isStart = True
      print('Car started...Ready to go!')
  elif req.lower() == 'stop':
    if not isStart:
      print('Car is readly stopped')
    else:
      isStart = False
      print('Car stopped.')
  elif req.lower() == 'quit':
    break
  else:
    print("I don't understand that")

# For loop
for item in 'Python':
  print(item)

for item in ['Mosh', 'John', 'Sarah']:
  print(item)

for item in range(5, 10, 2): # (start, end, step)
  print(item)

prices = [10, 20, 30]

total = 0
for price in prices:
  total += price

print(total)

# Nested Loop
for x in range(4):
  for y in range(3):
    print(f'({x}, {y})')

# Challenge
for i in [5, 2, 5, 2, 2]:
  # print('*' * i)
  output = ''
  for j in range(i):
    output += '*'
  print(output)

# Lists
names = ['Mark', 'Otis', 'John', 'Jenny']
print(names)
print(names[0]) # index
print(names[2:])

names[0] = 'King'
print(names)

numbers = [3, 6, 2, 8, 4, 10]
max_num = numbers[0]
for num in numbers:
  if num > max_num:
    max_num = num

print(max_num)

# 2D Lists
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

print(matrix[0][1])
for row in matrix:
  for item in row:
    print(item)

numbers = [5, 2, 1, 7, 4]
numbers.append(13)
numbers.insert(0, 20) # index, value
numbers.remove(20)
# numbers.clear()
numbers.pop()
print(numbers.index(5))
print(numbers)
print(50 in numbers)

numbers = [5, 2, 1, 5, 7, 4]
print(numbers.count(5))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)

# solution
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# new = { i: 0 for i in numbers }
# print(list(new.keys()))
uniques = []
for num in numbers:
  if num not in uniques:
    uniques.append(num)
print(uniques)

# Tupple
# can't remove, change

numbers = (1, 2, 3)
print(numbers[0])


# Unpacking
coordinates = (1, 2, 3)
# coordinates = [1, 2, 3]
x, y, z = coordinates
print(x, y, z)

# Dictionaries

customer = {
  "name": "Mark Nguyen",
  "age": 30,
  "is_verified": True
}

print(customer["name"])
print(customer.get("birthday", "Jan 1 1009")) # keys / default

customer["name"] = "Hiha"
customer["birthday"] = "1996"
print(customer)

# Function

def greet_user():
  print('Hi there!')
  print('Welcome aboard')

print('Start')
greet_user()
print('Finish')

# Parameter

def greet_user(first_name, last_name):
  print(f'Hi, {first_name} {last_name}')

greet_user('Mark', 'Nguyen')
greet_user(last_name='Nguyen', first_name='Mark')

# Return statement
def square(number):
  return number * number

print(square(number=3))

result = square(number=5)
print(result)

# by default python return None in function

# Handle Error

try:
  age = int(input('Age: '))
  risk = 2000 / age
  print(age)
except ZeroDivisionError:
  print('Age cannot be zero.')
except ValueError:
  print('Invalid value.')

# Comments

# Class
class Point:
  def move(self):
    print ("move")

  def draw(self):
    print("draw")

point1 = Point()
point1.draw()
point1.x = 1 # define new attribute
print(point1.x)

# Contructors
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def move(self):
    print ("move")

  def draw(self):
    print("draw")

point = Point(10, 20)
print(point.x) # is the same with point.x = 1 on above

# Inheritance

class Mammal:
  def walk(self):
    print("walk")

class Dog(Mammal):
  def bark(self):
    print("bark")

class Cat(Mammal):
  def be_annoying(self):
    print("annoying")

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.be_annoying()

# Module
# import converters
# converters.hello()

from converters import hello
hello()

# Package
from ecommerce.shipping import calc_shipping
calc_shipping()

# Generating Random Values
import random

for i in range(3):
  print(random.randint(10, 20))

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)

# Random output is a tupples

import random


class Dice:
  def roll(self):
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    return first, second


dice = Dice()
print(dice.roll())

# Files and Directory

from pathlib import Path


# Absolute path
# /user/local/bin
# Relative path
#

path = Path("emails")
print(path.exists())
print(path.mkdir())
print(path.rmdir())

path = Path()
print(list(path.glob('*.py')))


# Pypi and pip


# Machine Learning
# ML In Action

"""
"""
Steps:
  1. Import the Data
  2. Clean the Data
  3. Split the Data into Training/Test Sets
  4. Create a Model
  5. Train the Model
  6. Make Predictions
  7. Evaluate and Improve
"""

# Libraries
# Numpy 
# Pandas
# MatPlotLib
# Scikit-Learn

# Kaggle (dataset)
