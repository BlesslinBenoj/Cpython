#1

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

class ElectricCar(car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)

my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())


#2

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

class ElectricCar(car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"this car has a {self.battery_size} kwh battery.")

my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


#3

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

class ElectricCar(car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = battery()

my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()


#4

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

my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()































