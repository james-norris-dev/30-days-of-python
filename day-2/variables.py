""" Day 2 of 30 Days of Python
 Exercises - Day 2"""
import math

# Exercise Level - 1
first_name = 'Steve'
last_name = 'Smith'
full_name = first_name + ' ' + last_name
country = 'USA'
city = 'San Diego'
age = 22
year = 1983
is_married = False
is_true = True
is_light = False
name, grade, gender = 'Jason', 7, 'Male'

# Exercise Level - 2
print(type(first_name))
print(len(first_name))
print(type(last_name))
print(len(last_name) == len(first_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type(name))
print(type(grade))
print(type(gender))

num_one = 5
num_two = 4
plus_num = num_one + num_two
print(plus_num)
minus_num = num_one - num_two
print(minus_num)
mult_num = num_one * num_two
print(mult_num)
div_num = num_one / num_two
print(div_num)
mod_num = num_two % num_one
print(mod_num)
power_num = num_one ** num_two
print(power_num)
bottom_num = num_one // num_two
print(bottom_num)

radius = 30
area_of_circle = math.pi * radius ** 2
print(area_of_circle)
circum_of_circle = 2 * math.pi * radius
print(circum_of_circle)

user_input = input('Enter a radius: ')
area_of_circle = math.pi * int(user_input) ** 2
print(area_of_circle)

user_first_name = input('Enter your name: ')
user_last_name = input('Enter your last name: ')
user_country = input('Enter your country: ')
user_age = input('Enter your age: ')

help('keywords')




