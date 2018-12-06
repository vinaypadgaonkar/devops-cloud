class Car:
    def __init__(self):
        self.carFare = {'Hatchback': 30, 'Sedan': 50, 'SUV': 100}
        self.availableCars = self.carFare.keys()

    def displayAvailableCars(self):
        print('List of Available Cars:')
        for cars in self.availableCars:
            print(cars)

    def displayFareDetails(self):
        print('List of Cars types with its per day cost:')
        print('Hatchback: $', self.carFare['Hatchback'])
        print('Sedan: $', self.carFare['Sedan'])
        print('SUV: $', self.carFare['SUV'])

    def calculateFare(self, typeOfCar, period):
        return self.carFare[typeOfCar] * period

car = Car()

while True:
    print("Press 1 to display the available cars.")
    print("Press 2 to display the available cars with its fare details.")
    print("Press 3 to calculate the fare.")
    print("Press 4 to exit")
    userChoice = int(input())
    if userChoice is 1:
        car.displayAvailableCars()
    elif userChoice is 2:
        car.displayFareDetails()
    elif userChoice is 3:
        print("Enter the type of car:")
        carType = input()
        print("Enter the total number of days for the rent")
        timePeriod = int(input())
        rent = car.calculateFare(carType,timePeriod)
        print(f"Rental Details for your requested Car {carType} for {timePeriod} days is ${rent}")
        #print("Your rental details for the car ",carType, "taken for ",timePeriod,"is: $",rent)
    elif userChoice is 4:
        quit()
