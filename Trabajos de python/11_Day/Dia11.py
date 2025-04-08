# Exercises: Level 1
#1
def add_two_numbers(a,b):
    num=a + b
    return num
print (add_two_numbers(7,8))

#2
def area_circle(r):
    area=3.14*r**2
    return area

print (area_circle(96))

#3
def suma_total(*args):
    total = 0
    for arg in args:
        if not isinstance(arg, (int, float)): 
            return "All arguments must be numbers."
        total += arg
    return total
print (suma_total(1,2,46,53,98))

#4
def convertir_celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius_temp = 25
fahrenheit_temp = convertir_celsius_a_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")

#5
def check_season(month):
    if month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    elif month in ['September', 'October', 'November']:
        return 'Autumn'
print (check_season('August'))

#6
def calculate_slope(x1,y1,x2,y2):
    slope=(y2-y1)/(x2-x1)
    return slope
print (calculate_slope(19,29,38,40))

#7
def solve_quadratic_eqn(a,b,c):
    x1=(-b+((b**2)-4*a*c)**0.5)/(2*a)
    x2=(-b-((b**2)-4*a*c)**0.5)/(2*a)
    return x1,x2
print (solve_quadratic_eqn(7,6,3))

#8
def print_list(lst):
     for i in lst:
        print(i)
print_list([1,2,3,4,5])

#9
def reverse_list(lst):
    return lst[::-1]
print (reverse_list([1,2,3,4,5]))

#10
def capitalize_list(lista):
    return [i.upper() for i in lista]
print (capitalize_list(['Potato', 'Tomato', 'Mango', 'Milk']))

#11
def add_item(food_staff,comida):
    food_staff=['Potato', 'Tomato', 'Mango', 'Milk']
    food_staff.append(comida)
    return food_staff

print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Eggs'))

#12
def remove_item(food_staff,comida):
    food_staff=['Potato', 'Tomato', 'Mango', 'Milk']
    food_staff.remove(comida)
    return food_staff
print (remove_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Mango'))

#13
def sum_num(num1):
    for i in range(num1+1):
        for j in range(num1):
            i=i+j
    return i
print(sum_num(100))


#14
def sum_of_odds(num1):
    for i in range(num1+1):
        for j in range(num1):
            if i%2==0 and j%2==0:
                i=i+j
    return i
print(sum_of_odds(100))

#15
def sum_of_even(num):
    total = 0
    for i in range(num + 1):
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(100))

# Exercises: Level 2
#1
def evens_and_odds(n):
    evens = 0
    odds = 0

    for i in range(n + 1):  
        if i % 2 == 0:  
            evens += 1
        else:  
            odds += 1

    return f"The number of evens are {evens}. The number of odds are {odds}."
print(evens_and_odds(100))

#2
def factorial(fac):
    numb=1
    for i in range(1,fac+1):
        numb=i*numb
    return numb
print (factorial(6))

#3
def is_empty(lst):
    if len(lst) == 0:
        return True
print (is_empty([]))

#4
def calc_mean(nums):
    total_media=0
    for i in nums:
        total_media=total_media+i
        prom=total_media/len(nums)
    return prom
print (calc_mean([3,2,4,1,5,5,5,7]))

def calc_mediana(nums):
    mediana=nums[int(len(nums)/2)]
    return mediana
print (calc_mediana([3,2,4,1,5,5,5,7]))

def calc_moda(nums):
    from collections import Counter
    calc_mode=Counter(nums)
    return calc_mode.most_common(1)
print(calc_moda([3,2,4,1,5,5,5,7]))

def calc_rango(nums):
    nums.sort()
    range1=nums[0]
    range2=nums[int(len(nums)-1)]
    j=range(range1, range2)
    return j
print(calc_rango([3,2,4,1,5,5,5,7]))

def calc_varianza(nums):
    var = sum(nums) / len(nums)
    var_res = sum((i - var) ** 2 for i in nums) / len(nums)
    return var_res
print(calc_varianza([3,2,4,1,5,5,5,7]))

def calc_std(nums):
    var = sum(nums) / len(nums)
    var_res = sum((i - var) ** 2 for i in nums) / len(nums)
    std=var_res**0.5
    return std
print(calc_std([3,2,4,1,5,5,5,7]))

# Exercises: Level 3
#1
def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if (num%i)==0:
            print(num,' no es primo')
        else:
            print(num,' es primo')
    return ''
print(is_prime(9))

#2
def unique(lst):
    return len(set(lst))==len(lst)
print(unique([3,2,4,1,5,5,5,7]))

#3
def same(lista):
    list = iter(lista)
    tipo = type(next(list))
    if all((type(x) is tipo) for x in list): 
        print(True)
    else:
        print(False)
    return ''
print(same([1,2,3,4,'true']))

#4
def is_valid_python_variable(var_name: str) -> bool:

    if not var_name.isidentifier():
        return False
    
    return True
print(is_valid_python_variable('for'))

#5
from collections import Counter
from countries_data import countries_1  

def most_spoken_languages(data, top_n=10):
    language_counter = Counter()

    
    for country in data:
        language_counter.update(country["languages"])

    
    most_spoken = language_counter.most_common(top_n)
    return most_spoken


top_languages = most_spoken_languages(countries_1, top_n=10)
print("Top 10 most spoken languages:")
for language, count in top_languages:
    print(f"{language}: {count}")

from countries_data import countries_1
def most_populated_countries(data, top_n=10):
    sorted_countries = sorted(data, key=lambda x: x["population"], reverse=True)
    return sorted_countries[:top_n]
top_countries = most_populated_countries(countries_1, top_n=10)
print("Top 10 most populated countries:")
for country in top_countries:
    print(f"{country['name']}: {country['population']}")

print("revisado")