# Python Object-Oriented Programming

class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"

emp_1 = Employee('Mark', 'Nguyen')
emp_2 = Employee('Test', 'User')

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Mark'
# emp_1.last = 'Nguyen'

# emp_2.first = 'Test'
# emp_2.last = 'User'

print(emp_1.fullname())
print(emp_1.email)

print(emp_2.fullname())
print(emp_2.email)

# Same
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))