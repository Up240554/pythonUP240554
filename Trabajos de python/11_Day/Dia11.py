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


    