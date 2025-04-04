ountries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1
#1
#Map fuction
def square(num):
    return num**2
print(list(map(square, numbers)))

def upper(name):
    return name.upper()
print(list(map(upper, names)))

#Filter function
def is_even(num):
    return num % 2 == 0
print(list(filter(is_even, numbers)))

def has_land(country):
    return 'land' in country.lower()
print(list(filter(has_land, countries)))

#Reduce function
from functools import reduce

def add(x, y):
    return x + y

total = reduce(add, numbers)
print(total)

#2
#Higher order function
def higher_order_function(func, arg):
    return func(arg)
print(higher_order_function(square, 5))

#Closure
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
print(outer_function(5)(10))

#Decorator
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def multiply(a, b):
    return a * b

print(add(5, 3))
print(multiply(4, 6))

