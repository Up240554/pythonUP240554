age = int(input("Escribe tu edad "))
print("")
height = float(input("Escribe tu altura "))
print("")
##3
complex = complex(input("Un numero complejo "))

##4 Triangle
print("")
base = int(input("Ingresa la base de tiengulo "))
heightT = int(input("Ingresa la altura del triangulo "))
area = float((base * heightT)/2)
print("El area de tu triangulo es: ", area)

##5 Perimeter
print("")
lado1 = int(input("El primer lado es: "))
lado2 = int(input("El segundo lado es: "))
lado3 = int(input("El tercer lado es: "))
perimeter = lado1 + lado2 + lado3
print("El perimetro del triangulo es de: ", perimeter)

##6 Length and Width
print("")
Length = int(input("Ingresa el valor del largo: ")) ##Largo
Width = int(input("Ingresa el valor del ancho: ")) ##Ancho
area1 = Length * Width
perimeter1 = 2 * (Length + Width)
print("El perimetro es de: ", perimeter1)

##7 Radius
print("")
radius = float(input("Ingresa la circunferencia de tu circulo: "))
pi = float(3.1416)
areac = float(pi * radius * radius)
circunference = float(2 * pi * radius)
print("Tu area es de: ", areac)
print("Tu circunferencia es de: ", circunference)

##8 Slope
print("")
print("Interaccion de la pendiente:")
pendiente = 2 ##la pendiente  de la ecuacion
intY = -2     ##Interaccion con eje y
intX = intY / pendiente  ##Interaccion con eje x
print("La pendiente de la ecuacion es: ", pendiente)
print("La interacción es de: ", intX) 

##9 Euclidean distance
print("")
x1 = 2
x2 = 6
y1 = 2
y2 = 10
distance = ((x2 - x1)**2 + (y2-y1)**2)**0.5
print("La distancia entre los dos puntos es: ", distance)
slope = (y2 - y1) / (x2 - x1)
print("The slope is: ", slope)

##10 Compare
print("")
Compare = pendiente <= slope
print("La diferencia entre las pendientes es de: ", Compare)

##11 Value Y
print("")
vaX = int(input("Ingresa el valor de X "))
vaY = (vaX**2 + (6 * vaX) + 9) 
print("El valor de la variable Y es igual a ", "|", vaY, "|")

##12
print("")
##python = int(input("Ingresa el valor de python "))
##dragon = int(input("Ingresa el valor de dragon "))
python = str(55)
dragon = str(3)

comp = python == dragon
print(len(python))
print(len(dragon))
print("La comparación de los numeros fue: ", comp)

##13
print("")

on = ("python", "dragon")
if  "dragon" in on:
    print("on is in dragon")
if  "python" in on:
    print("on is in dragon")

##14 Jargon
print("")
course = ("I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.")
if "jargon" in course:
    print("jargon is in the sentence")

##15 
print("")
py = ("the tv is off")
dra = ("the tv is off")
if "on" in py and dra:
    print("on is in the sentence")
else: 
    print("on isn´t in these sentens")

##16
print("")
print("Una prueba de longitud con la funcion len")
text = str(float("654864643215"))
len(text)
print("La longitud de la frase es de: ", len(text))

##17
print("")
par = int(input("Ingresa un numero: "))
par = (par % 2)
if par > 0:
 print("Es numero inpar")

else:
    print("Es numero par")


##18
print("")
floDiv = 7 // 3
intPi = int(2.7)
comDiv = floDiv == intPi

print("El resultado de la division es:", comDiv)

##19 
print("")
ty1 = type("10")
ty2 = type(10)
comTy = ty1 == ty2
print("Los tipos de las unidades son iguales? ", comTy)

##20 
print("")
typ1 = int(float("9.8"))
typ2 = 10
comTyp = typ1 == typ2
print("Los tipos de las unidades son iguales? ", comTyp)

##21
print("")
hours = int(input("Ingresa las horas que trabajaste: "))
rate = int(input("Ingresa el valor de la tarifa por hora: "))
salario = hours * rate
print("Tu salario es de ", "|", salario, "|" )

##22 
print("")
years = int(input("Cuantos anos tienes? "))
seconds = (365 * (3600*24))
total = (years * seconds)
print("Tu tienes un total de:", total, "segundos")

##23
for i in range(1, 6):  # Genera números del 1 al 5
    print(f"{i:<7} {1:<11} {i:<11} {i**2:<11} {i**3:<11}")


#Ejemplo 23.1
for i in range(1, 6):  # Números del 1 al 5
    print(i, 1, i, i**2, i**3)

print("revisado")