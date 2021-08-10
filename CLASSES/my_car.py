from car import car

my_new_car = car('audi','a6',2017)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()