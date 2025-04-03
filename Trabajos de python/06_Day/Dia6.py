#1
tuple = ()

#2
hermanos = ("Kevin", "Alonso")
hermanas = ("Renata", "Jacqueline")

#3
siblings = hermanas + hermanos
print(siblings)

#4
number_of_siblings = len(siblings)
print("Number of siblings:", number_of_siblings)

#5
parents = ("Marco", "Denisse")
Family_members = parents + siblings
print(Family_members)

##level 2
#1
Family_members = ('Marco', 'Denisse', 'Renata', 'Jacqueline', 'Kevin', 'Alonso')
parents = Family_members[:2]
siblings = Family_members[2:]
print(parents)
print(siblings)

#2
frutas = ("Manzana", "Plátano", "Naranja", "Mango")
verduras = ("Zanahoria", "Brócoli", "Tomate", "Papa")
productos_animales = ("Leche", "Huevos", "Queso", "Pollo")
food_stuff_tp = frutas+verduras+productos_animales
print(food_stuff_tp)

#3
food_stuff_lt = list(food_stuff_tp)

#4
print(food_stuff_tp[7:8])

#5
first_three_items = food_stuff_tp[:3]
last_three_items = food_stuff_tp[-3:]
print("first_three_items", "last_three_items")

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Norway' in nordic_countries)
print('Denmark' in nordic_countries)

print("revisado")