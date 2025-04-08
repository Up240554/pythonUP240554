countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
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

#3
def func(num):
    return num ** 3
print(list(map(func, numbers)))

#4
for i in countries:
    print(i)

#5
for i in names:
    print(i)

#6
for i in numbers:
    print(i)

# Exercises: Level 2
#1
upp=list(map(str.upper, countries))
print(upp)

#2
def square(num):
    return num**2
print(list(map(square, numbers)))

#3
uppi=list(map(str.upper, names))
print(uppi)

#4
def has_land(country):
    return 'land' in country.lower()
print(list(filter(has_land, countries)))

#5
six__countries = list(filter(lambda country: len(country) >= 6, countries))
print(six__countries)

#6
def stars_with_e(country):
    return country.startswith('E')
print(list(filter(stars_with_e, countries)))

#7
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


result = reduce(
    lambda x, y: x + y, 
    filter(
        lambda x: x % 2 == 0,  
        map(
            lambda x: x ** 2,  
            numbers
        )
    )
)

print(result)

#8
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

mixed_list = [1, 'hello', 3.14, 'world', True, 'Python']
string_list = get_string_lists(mixed_list)
print(string_list)

#9
from functools import reduce

def add(x, y):
    return x + y

total = reduce(add, numbers)
print(total)

#10
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
sentence = reduce(
    lambda acc, country: acc + ', ' + country if country != countries[-1] else acc + ', and ' + country, countries[:-1],countries[0]) + ' are north European countries.'
print(sentence)

#11
from lista_paises import countries_2  
countries_with_land = list(filter(lambda country: 'land' in country.lower(), countries_2))
print(countries_with_land)

#12
from lista_paises import countries_2
def count_countries_by_letter(countries):
    country_count = {}
    for country in countries:
        first_letter = country[0].upper()  
        if first_letter in country_count:
            country_count[first_letter] += 1
        else:
            country_count[first_letter] = 1
    return country_count

country_letter_count = count_countries_by_letter(countries_2)
print(country_letter_count)

#13
from lista_paises import countries_2 
def get_first_ten_countries(countries):
    return countries[:10] 

first_ten_countries = get_first_ten_countries(countries_2)
print(first_ten_countries)

#14
from lista_paises import countries_2 
def get_last_ten_countries(countries):
    return countries[-10:]  

last_ten_countries = get_last_ten_countries(countries_2)
print(last_ten_countries)

# Exercises: Level 3

from countries_data import countries_1
#1
def sort_countries_by_name(countries):
    return sorted(countries, key=lambda x: x['name'])

sorted_countries = sort_countries_by_name(countries_1)
print("Countries sorted by name:")
for country in sorted_countries:
    print(country['name'])

#2
def most_spoken_languages(countries, top_n=10):
    from collections import Counter
    language_counter = Counter()
    for country in countries:
        language_counter.update(country['languages'])
    return language_counter.most_common(top_n)

most_spoken = most_spoken_languages(countries_1, 10)
print("\nTen most spoken languages:")
for language, count in most_spoken:
    print(f"{language}: {count}")

#3
def most_populated_countries(countries, top_n=10):
    return sorted(countries, key=lambda x: x['population'], reverse=True)[:top_n]

most_populated = most_populated_countries(countries_1, 10)
print("\nTen most populated countries:")
for country in most_populated:
    print(f"{country['name']}: {country['population']}")

print("revisado")