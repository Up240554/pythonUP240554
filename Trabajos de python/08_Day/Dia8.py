#1
dog = {}

#2
dog["name"] = "Paco"
dog["color"] = "Negro"
dog["breed"] = "Dobberman"
dog["legs"] = 4
dog["age"] = 1

#3
Alumno= {"Nombre": "Diego",
    "Apellido": "Lopez",
    "Genero": "Masculino",
    "Edad": "19",
    "Estado civil": "Soletero",
    "Habilidades":["Liderazgo",],
    "Pais": "Mexico",
    "Ciudad": "Aguascalientes",
    "Direccion": "de los Flamingos 107"}
print("Alumno")

#4
print (len(Alumno))

#5
print(list(Alumno['Habilidades']))

#6
Alumno["Habilidades"].extend(["Resolución de problemas"])
print("Alumno")


#7
keys_list = list(Alumno.keys())
print("Claves del diccionario Alumno:", keys_list)

#8
values_list = list(Alumno.values())
print("Valores del diccionario Alumno:", values_list)

#9
Estudiantes= list(Alumno.items())
print(Estudiantes)

#10
del Alumno ["Direccion"]
print(Alumno)

#11
del dog
print("revisado")