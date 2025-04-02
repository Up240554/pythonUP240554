#1
print("ingresa tu edad")
edad=int(input())
if edad > 17:
     print("puedes aprender a manejar")
else:
     print("no puedes manejar te faltan", 18-edad)

#2
print("Ingresa tu edad")
myage = 18
yourage = int(input())
if yourage > myage:
    print("Eres", yourage - myage, "años más grande que yo")

elif yourage < myage:
    print("Eres", myage - yourage, "años más chico que yo")

else:
    print("Tenemos la misma edad")

#3
print("ingresa un num")
n1=int(input())
print("ingresa un num")
n2=int(input())
if n1 < n2:
    print(n2, " es mayor a ", n1)
elif n1 > n2:
     print(n2, " es menor a ", n1)
else:
     print(n2, " es igual a ", n1)

#Exercises: Level 2
#1
print("ingresa tu calificación")
calificación=int(input())
if 80<calificación<100: print("tu nota es A")
elif 70<calificación<89: print("tu nota es B")
elif 60<calificación<69: print("tu nota es C")
elif 50<calificación<59: print("tu nota es D")
elif 0<calificación<49: print("tu nota es F")
else: print("la calificacion ingresada no es valida")

#2
print("ingresa el mes del año")
mes= input()
if mes in["septiembre", "octubre", "noviembre"]: print("la estacion es otoño")
elif mes in["diciembre", "enero", "febrero"]: print("la estacion es invierno")
elif mes in["marzo", "abril", "mayo"]: print("la estacion es primavera")
elif mes in["junio","julio", "agosto"]: print("la estacion es verano")
else: print("el texto ingresado no corresponde con un mes")

#3
frutas = ['banana', 'orange', 'mango', 'lemon']
lista_de_frutas = input("Ingrese una fruta: ").lower()
if lista_de_frutas in frutas:
    print("la fruta ya esta en la lista")
else:
    frutas.append(lista_de_frutas)
    print("fruta agregada a la lista.")
    print("Lista actulizada:", frutas)
    
#Exercises: Level 3
person={
    'first_name': 'Abner',
    'last_name': 'Muro',
    'age': 22,
    'country': 'Belice',
    'is_marred':  False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Avenida siempre viva',
        'zipcode' : '20000'
    }
    }
#1
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) 
    print("Middle skill:", skills[middle_index])
else:
    print("The person dictionary does not have the 'skills' key.")

#2
if 'skills' in person:
    skills = person['skills']
    if 'Python' in skills:
        print("The person has the 'Python' skill.")
    else:
        print("The person does not have the 'Python' skill.")
else:
    print("The person dictionary does not have the 'skills' key.")

#3
if 'skills' in person:
    skills = person['skills']
    if set(skills) == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif set(['Node', 'Python', 'MongoDB']).issubset(skills):
        print('He is a backend developer')
    elif set(['React', 'Node', 'MongoDB']).issubset(skills):
        print('He is a fullstack developer')
    else:
        print('unknown title')
else:
    print("The person dictionary does not have the 'skills' key.")

#4
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
else:
    print(f"{person['first_name']} {person['last_name']} does not meet the criteria.")
    