##
lst=list()

##
mandado=['manzana', 'pera', 'platano', 'uva', 'naranja']

##
print(len(mandado))

##
print(mandado[0])
print(mandado[2])
print(mandado[4])

##
mixed_data_types=['Abner', '18', '1.75', 'soltero', 'Orion, 116']

##
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

##
print(it_companies) 

##
print(len(it_companies))

##
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

##
del it_companies[0]
it_companies.insert(0, 'Twitter')
print(it_companies)

##
it_companies.append('IBM')

##
it_companies.insert(3, 'Samsung')

##
it_companies[0]=it_companies[0].upper()
print(it_companies)

##
print(str.join('#;', it_companies))

##
existe='Facebook' in it_companies
print(existe)

##
it_companies.sort()
print(it_companies)

##
it_companies.reverse()
print(it_companies)

##
companies1=it_companies[0:3]
print(companies1)

##
companies2=it_companies[6:9]
print(companies2)

##
companies3=it_companies[4:5]
print(companies3)

##
print(it_companies.remove('Samsung'))

##
print(it_companies.remove('IBM'))

##
print(it_companies.remove('Oracle'))

##
print(it_companies.remove('Amazon'))

##
del (it_companies)

##
ront_end=['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end=['Node', 'Express', 'MongoDB']
total=ront_end+back_end
print(total)   

##
full_stack=total.copy()
print(full_stack)

##Nivel 2

##
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
del ages[0:2]
del ages[7:8]
print(ages)
ages.append(19)
ages.append(19)
ages.append(26)
print(ages)

prom=(sum(ages)/len(ages))
print(prom)
ages.sort()
print(abs(ages[0]-prom))
print(abs(ages[8]-prom))

from lista_paises import countries
print(countries[int(len(countries)/2)])
list1=countries[0:96]
list2=countries[96:192]

paises=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_three=paises[0:3] 
rest=paises[3:7]
print(first_three)
print(rest)

print("revisado")