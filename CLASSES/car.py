#1

class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = car('audi','a4',2019)
print(my_new_car.get_descriptive_name())


#2

class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles in it.")

my_new_car = car('corvette','zr1',2005)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


#3

class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles in it.")

my_new_car = car('corvette','zr1',2005)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 25
my_new_car.read_odometer()


#4

class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles in it.")

    def update_odometer(self,mileage):
        self.odometer_reading = mileage

my_new_car = car('corvette','zr1',2005)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(25)
my_new_car.read_odometer()

#5

class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 2500

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles in it.")

    def update_odometer(self,mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You cant roll back on odometer")

my_new_car = car('corvette','zr1',2005)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(1900)
my_new_car.read_odometer()


#6

class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 25000

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles in it.")

    def update_odometer(self,mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You cant roll back on odometer")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

my_used_car = car('lamborghini','gallardo',2017)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(25500)
my_used_car.read_odometer()

my_used_car.increment_odometer(200)
my_used_car.read_odometer()

#7

class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 25000

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles in it.")

    def update_odometer(self,mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You cant roll back on odometer")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

#8

class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 25000

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles in it.")

    def update_odometer(self,mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You cant roll back on odometer")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

class battery:
    def __init__(self,battery_size = 75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size} kwh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = battery()


















