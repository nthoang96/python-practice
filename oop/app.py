# Using class create object
# Note: Constructor always run when call class

# Encapsulation
# Inheritance
# Polymorphism

# Example
class User:
  def log(self):
    print("Users")

class Teacher(User):
  def log(self):
    print("I'm a Teacher!")

class Customer(User):

  def log(self):
    print("I'm a Customer!")

  def __init__(self, name, membership_type):
    self.name = name
    self.membership_type = membership_type

  @property
  def name(self):
    """
    Getting name
    """
    return self._name

  @name.setter
  def name(self, name):
    """
    Setting name
    """
    self._name = name

  @name.deleter
  def name(self):
    """
    Delete name
    """
    del self._name

  def update_membership(self, new_membership):
    self.membership_type = new_membership

  def read_customer():
    print("Reading customer from DB")

  def __str__(self):
    print("Converting to string")
    return f'{self.name} {self.membership_type}'

  def print_all_customers(customers):
    for customer in customers:
      print(customer)

  def __eq__(self, other):
    if self.name == other.name and self.membership_type == other.membership_type:
      return True
    return False

  __hash__ = None
  __repr__ = __str__

customers = [Customer("Caleb", "Gold"), Customer("Brad", "Bronze"), Teacher()]

# customers[1].verified = False
# print(customers[1].verified)

print(customers[1].membership_type)
customers[1].update_membership("Gold") # similar with customer.membership_type = "Gold"
print(customers[1].membership_type)

# Function not argument self
Customer.read_customer()

# Convert to string
print(customers[1])

Customer.print_all_customers(customers)

# Equal
print(id(customers[0]), id(customers[1]))
print(customers[0] == customers[1])

# Hash
print(customers)


#
# del customers[0].name 
print(customers[1].name)

customers[0].log()

for i in customers:
  i.log()