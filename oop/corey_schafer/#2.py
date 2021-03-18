class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@example.com"

        Employee.num_of_emps += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

emp_1 = Employee('Mark', 'Nguyen', 50000)
emp_2 = Employee('User', 'Test', 60000)

# Employee.raise_amount = 1.05
emp_1.raise_amount = 1.05

# print(Employee.__dict__)
# print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)