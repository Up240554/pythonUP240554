# Exercises: Level 1
#1
import random
import string

def random_user():
    characters = string.ascii_letters + string.digits 
    user_id = str(''.join(random.choice(characters) for _ in range(6))) 
    return user_id
print(random_user()) 

#2
import random
import string
def random_user_id():
    try:
        num_char = int(input('Enter the number of characters for the user ID: '))
        num_user = int(input('Enter the number of user IDs to generate: '))
        for i in range(num_user):
            user_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(num_char))
            print(user_id)
    except ValueError:
        print("Please enter valid integers for both inputs.")

random_user_id()

#3
def rgb():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    return r,g,b
print(rgb())

# Exercises: Level 2
#1
def hexa_color():
   for i in range(6):
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    print(hex_color)
hexa_color()

#2
def list_of_rgb():
    try:
        colors = []
        num_colors = int(input('Enter the number of colors to generate: '))
        for i in range(num_colors):
         r=random.randint(0, 255)
         g=random.randint(0, 255)
         b=random.randint(0, 255)
         colors.append((r,g,b))
        print(colors)
    except ValueError:
        print("Please enter a valid integer for the number of colors.")
list_of_rgb()

#3
def generate_colors():
   try:
    color=str(input('Which color do you want to generate?')).upper()
    num=int(input('How many colors do you want to generate?'))
    colors = []
    if color=='RGB':
        for i in range(num):
            r=random.randint(0, 255)
            g=random.randint(0, 255)
            b=random.randint(0, 255)
            colors.append((r,g,b))
        print(colors)
    else:
        for i in range(num):
            r=random.randint(0, 255)
            g=random.randint(0, 255)
            b=random.randint(0, 255)
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            colors.append(hex_color)
        print(colors)
   except ValueError:
        print("Please enter a valid integer for the number of colors.")
generate_colors()

#Exercises: Level 3
#1
def shuffle_list():
    lista=['Potato', 'Tomato', 'Mango', 'Milk']
    random.shuffle(lista)
    print(lista)
    return lista
shuffle_list()

#2
import random
def numbers():
    generated_numbers = []
    while len(generated_numbers) < 7:
        num = random.randint(0, 9)
        if num not in generated_numbers:
            generated_numbers.append(num)
    return generated_numbers
print(numbers())