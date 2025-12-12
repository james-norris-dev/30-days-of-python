""" Day 1 of 30 Days of Python
 Exercises - Day 1
 Exercise: Level 2"""

# Using different operations on the operands 3 and 4
print(4 + 3)
print(4 - 3)
print(3 - 4)
print(4 * 3)
print(4 % 3)
print(3 % 4)
print(4 / 3)
print(3 / 4)
print(4 ** 3)
print(3 ** 4)
print(4 // 3)
print(3 // 4)

print('')
# Writing strings to the python interactive shell
print('Jame')
print('Norris')
print('USA')
print('I am enjoying 30 days of python')

print('')
# Checking the type - with function 'type()'
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Your name'))
print(type('Your family name'))
print(type('Your country'))

print('')
print(f"12, Integer (int)")
print(type(12))
print(f"12.3456, Float (float)")
print(type(12.3456))
print(f"My name, String (str)")
print(type("My name"))
print(f"True, Boolean (bool)")
print(type(True))
# Lists - [], a mutable ordered collection, can hold multiple data types
example_list = [12, 12.3456, 'My name', True]
print(f"{example_list}, List (list)")
print(type(example_list))
# Tuples - (), an immutable ordered collection, can hold multiple data types
example_tuple = (12, 12.3456, 'My name', True)
print(f"{example_tuple}, Tuple (tuple)")
print(type(example_tuple))
# Set - {}, a mutable unordered collection - no duplicates
example_set = {12, 12.3456, 'My name', True}
print(f"{example_set}, Set (set)")
print(type(example_set))
# Dictionary - {}, an immutable ordered collection of key_value pairs - keys are case sensitive
example_dict = {'integer': 12,
                'float': 12.3456,
                'string': 'My name',
                'boolean': True}
print(f"{example_dict}, Dict (dict)")
print(type(example_dict))


