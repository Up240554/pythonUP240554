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
fila=0
columna=8

for i in range(fila):
    for j in range(columna):
        print('#', end='')
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