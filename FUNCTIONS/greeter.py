
#1

def greet_user():
    print("Hello!")

greet_user()

#2

def greet_user(username):
    print(f"Hello {username.title()}.")

greet_user('logictenacity')

#3

def describe_pet(animal_type,pet_name):
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')

#4

def describe_pet(animal_type,pet_name):
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog','panny')


#5
def describe_pet(animal_type,pet_name):
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry','hamster')
#6
def describe_pet(animal_type,pet_name):
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name = 'harry',animal_type = 'hamster')
describe_pet(animal_type = 'hamster',pet_name = 'harry')

#7
def describe_pet(pet_name, animal_type = 'dog'):
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name = 'williams')

#8
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease enter your name: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello {formatted_name}!")

#9

def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' to quit at any time)")

    f_name = input("First name: ")
    if f_name == 'q' :
        break

    l_name = input("Last name: ")
    if l_name == 'q' :
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello {formatted_name}!")














