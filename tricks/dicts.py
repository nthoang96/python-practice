# Because Python has first-class functions they can
# be used to emulate switch/case statements

def dispatch_if(operator, x, y):
  if operator == 'add':
    return x + y
  elif operator == 'sub':
    return x - y
  elif operator == 'mul':
    return x * y
  elif operator == 'div':
    return x / y
  else:
    return None

def dispatch_dict(operator, x, y):
  return {
    'add': lambda: x + y,
    'sub': lambda: x - y,
    'mul': lambda: x * y,
    'div': lambda: x / y,
  }.get(operator, lambda: None)()

print(dispatch_dict('add', 1, 1))


a = {'a': 1, 'b': 2}
b = {'b': 3, 'c': 4}
z = {**a, **b}
print(z)