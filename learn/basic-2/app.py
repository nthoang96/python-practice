"""
# Variables
a = 5
print(a)

b = "hello"
print(b)

credit_card = 4412312312312312323
print(credit_card)

import turtle

qazi_turtle = turtle.Turtle()

qazi_turtle.forward(100)
qazi_turtle.right(90)
qazi_turtle.forward(100)
qazi_turtle.right(90)
qazi_turtle.forward(100)
qazi_turtle.right(90)
qazi_turtle.forward(100)

turtle.done()

# Functions
import turtle

qazi_turtle = turtle.Turtle()

def square():
  qazi_turtle.forward(100)
  qazi_turtle.right(90)
  qazi_turtle.forward(100)
  qazi_turtle.right(90)
  qazi_turtle.forward(100)
  qazi_turtle.right(90)
  qazi_turtle.forward(100)

square()
qazi_turtle.forward(200)
square()

turtle.done()

# Calendar

import calendar

print(calendar.weekheader(3))
print(calendar.firstweekday())
print(calendar.month(2020, 9))
print(calendar.monthcalendar(2020, 9))
print(calendar.calendar(2020))

is_leap = calendar.isleap(2020)
print(is_leap)

how_many_leap_days = calendar.leapdays(2000, 2020)
print(how_many_leap_days)

"""

# if else statements
elephant_weight = 3000
ant_weight = 0.1
if elephant_weight > ant_weight: # True
  print("That right!")
else:
  print("Haha, you're wrong!")

# While Loop