class Vehicle:
#define vehicle class    
    def __init__vehicle_make(self, make, model):
        #initialize class attributes
        self.make = make
        self.model = model
    #return set attributes
    def __init__display_vehicle(self):
        print(f"The make is: {self.make}")
        print(f"The model is: {self.model}")

class Car(Vehicle):
    #set car attributes
    def __init__car_door(self, doors):
        self.doors = doors
    #return set attributes
    def __init__display_vehicle(self):
        print(f"The car make is: {self.make}")
        print(f"The car model is: {self.model}")
        print(f"The number of doors is: {self.doors}")

class Pickup(Vehicle):
    #set pickup attributes
    def __init__bed_length(self, length):
        self.length = length
    #return set attributes
    def __init__display_vehicle(self):
        print(f"The truck make is: {self.make}")
        print(f"The truck model is: {self.model}")
        print(f"The bed length is: {self.length}")

print(f"Welcome to Virtual Garage")
prompt = "\nEnter 1 to make a car, 2 to make a truck, and 3 to quit: "

option = ""
while option != 3:
    option = input(prompt)

    if option == 1:
        input_car_make = input("Please enter the car make: ")
        input_car_model = input("Please enter the car model: ")
        input_door = input("Please enter the number of doors: ")
        new_car = Car()
        new_car.display_vehicle(input_make)
        new_car.display_vehicle(input_model)
        new_car.car_door(input_door)
        print(f"\nThe car has been added to the garage.")
    elif option == 2:
        input_pickup_make = input("Please enter the picku make: ")
        input_pickup_model = input("Please enter the pickup model: ")
        input_bed_length = input("Please enter the bed length: ")
        new_pickup = Pickup()
        new_pickup.display_vehicle(input_pickup_make)
        new_pickup.display_vehicle(input_pickup_model)
        new_pickup.bed_length(input_bed_length)
        print(f"The pickup has been added to the garage.") 
    else:
        main