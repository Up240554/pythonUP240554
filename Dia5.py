# Declare an empty list
list = []

# Declare a list with more than 5 items
comida = ["alitas", "pan", "papas", "manzanas", "huevos", "pollo"]

# Find the length of your list
print(len(comida))

#Get the first item, the middle item and the last item of the list
print(comida[1])
print(comida[4])
print(comida[5])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = [ "Diego", "19", "1.70", "Soltero", "de los flamingos, 107"]

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#Print the list using _print()_
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

#Print the first, middle and last company
print(it_companies[1])
print(it_companies[4])
print(it_companies[7])

# Print the list after modifying one of the companies
del it_companies[3]
it_companies.insert(3, "Tesla")
print(it_companies)

#Add an IT company to it_companies
it_companies.append("Twitter")

#Insert an IT company in the middle of the companies list
it_companies.insert(3, 'Sony')

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()

#Join the it_companies with a string '#;&nbsp; '
print(str.join('#&', it_companies))

#Check if a certain company exists in the it_companies list.
existe='Tesla' in it_companies
print(existe)

#Sort the list using sort() method
it_companies.sort()
print(it_companies)

#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#Slice out the first 3 companies from the list
companies1=it_companies[0:3]
print(companies1)

#Slice out the last 3 companies from the list
companies2=it_companies[6:9]
print(companies2)

#Slice out the middle IT company or companies from the list
companies3=it_companies[4:5]
print(companies3)

#Remove the first IT company from the list
print(it_companies.remove('Tesla'))

# Remove the middle IT company or companies from the list
print(it_companies.remove('IBM'))

# Remove the last IT company from the list
print(it_companies.remove('Amazon'))

#Remove all IT companies from the list
ront_end=['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end=['Node', 'Express', 'MongoDB']
total=ront_end+back_end
print(total)   

#Join the following lists:
full_stack=total.copy()
print(full_stack)

#level 2
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