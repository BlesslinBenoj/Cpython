#1

from car import car,ElectricCar

my_vehicle = car('corvette','zr1',2005)
print(my_vehicle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())

#2

import car

my_vehicle = car.car('corvette','zr1',2005)
print(my_vehicle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())

#3

from car import car
from electric_car import ElectricCar


my_vehicle = car('corvette','zr1',2005)
print(my_vehicle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())


#4

from electric_car import ElectricCar as EC

my_tesla = EC('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())



























