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

