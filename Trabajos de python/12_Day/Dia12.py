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
