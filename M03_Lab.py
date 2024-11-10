class Vehicle: #This is the super class, which initializes the vehicle type
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
    

class Automobile(Vehicle): #this class takes the vehicle from the super class and gets its information

    def __init__(self, vehicle_type, year, make, model, doors, roof): #this functino is intitializing the infoormation for the vehicle
        super().__init__(vehicle_type)

        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_vehicle(self): #this functino gives the user-friendly display of the vehicle's information
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

def main():
    vehicle_type = "car" #for this scenario, we initialized the vehicle to be car 

    print("Please provide us the information about your car")

    year = input("What is your vehicle's year? ") #gets uer input for year
    make = input("What is your vehicle's make? ") #gets uer input for make
    model = input("What is your vehicle's model? ") #gets uer input for model
    doors = input("How many doors does your vehicle have? ") #gets uer input for number of doors
    roof = input("What type of roof does your vehicle have? (ex. solid or sun roof) ") #gets uer input for type of roof
    print("\n")

    vehicle = Automobile(vehicle_type, year, make, model, doors, roof) #takes the user inputs and uses the classes to display the information

    vehicle.display_vehicle() #displays the vehicle information

if __name__ == "__main__": #runs the main function
    main()