#1

class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = dog('willie',6)
my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")

#2


class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


my_dog = dog('willie',6)
your_dog = dog('lucy',3)

print(f"my dog's name is {my_dog.name}.")

print(f"my dog is {my_dog.age} years old")
my_dog.sit()

print(f"\nYour dog name is {your_dog.name}.")
print(f"your dog is {your_dog.age} years old")
your_dog.sit()





















