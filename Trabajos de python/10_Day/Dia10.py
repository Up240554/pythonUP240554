#1
count=0
while count<11:
    print(count)
    count=count + 1

numbers=[1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    print(i)

#2
while -1<count:
    print(count)
    count=count - 1

inum=[10,9,8,7,6,5,4,3,2,1]
for i in inum:
    print(i)

#3
gato=0
while gato<8:
    print('#'*int(gato))
    gato=gato + 1

#4
fila=8
columna=8

for i in range(fila):
    for j in range(columna):
        print('#', end=' ')
    print()

#5
num=0

while num<11:
    print(num, 'x', num, '=', num*num)
    num=num + 1

#6
nom=['Python', 'Numpy','Pandas','Django', 'Flask'] 
for i in nom:
    print(i)

#7
for i in range(101):
    if i%2==0:
        print(i)

for i in range(101):
    if i%2!=0:
        print(i)

i=0

# Exercises: Level 2

#1
total_sum = 0
for i in range(101):
    total_sum += i
print(total_sum)

#2
sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i
print("Sum of even numbers:", sum_evens)
print("Sum of odd numbers:", sum_odds)

# Exercises: Level 3
#1
from lista_paises import countries
paisesland=[countries for countries in countries if 'land' in countries]
print(paisesland)

#2
fruits = ['banana', 'orange', 'mango', 'lemon']
conteo=-1
for i in fruits:
    print(fruits[conteo])
    conteo=conteo -1

#3
from countries_data import countries_1

all_languages = set()
for country in countries_1:
    all_languages.update(country['languages'])
total_languages = len(all_languages)
print("Total number of languages:", total_languages)

#4
language_count = {}
for country in countries_1:
    for language in country['languages']:
        language_count[language] = language_count.get(language, 0) + 1

most_spoken_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]
print("Ten most spoken languages:")
for language, count in most_spoken_languages:
    print(f"{language}: {count}")

most_populated_countries = sorted(countries_1, key=lambda x: x['population'], reverse=True)[:10]
print("Ten most populated countries:")
for country in most_populated_countries:
    print(f"{country['name']}: {country['population']}")

print("revisado")