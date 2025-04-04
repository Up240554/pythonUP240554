# Exercises: Day 13
#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers=[i for i in numbers if 0>=i]
print(numbers)

#2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lists=[i for sublist in list_of_lists for inner_list in sublist for i in inner_list]
print(lists)

#3
lst=[(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(lst)

#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
capital1 = [[country.upper(), country[:3].upper(), capital.upper()] 
                       for sublist in countries for country, capital in sublist]
print(capital1)

#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
capital2 = [[country.upper(), capital.upper()] 
                       for sublist in countries for country, capital in sublist]
data=[{'country': country, 'capital': capital} for sublist in countries for country, capital in sublist]
print(data)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [f"{first} {last}" for sublist in names for first, last in sublist]
print(concatenated_names)

#7
slope=(lambda x1, y1, x2, y2: ((x2 - x1) / (y2 - y1) ))(3, 4, 5, 7)
print(slope)