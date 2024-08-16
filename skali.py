#driver in this cass is not the driver class that starts the app but the user who is driving the car
#gonna need to change this class name but fk it
#maybe add role to user instead of this
class driver:
    def __init__ (self, userID, name, carPlate, fuelType):
        self.userID = userID
        self.name = name
        self.carPlate = carPlate

class passenger:
    def __init__ (self, userID, name):
        self.userID = userID
        self.name = name
#class ride or class trip ?
class ride:
    def __init__(self, rideID, driver, passenger, date, time, startP, endP, fare, distance, status):
        self.rideID = rideID
        self.driver = driver
        self.passenger = passenger
        self.date = date
        self.time = time
        self.startP = startP
        self.endP = endP
        self.fare = fare
        self.distance = distance
        self.status = status
#only leader can remove or add people
def addPassenger(userID, name):
    return passenger(userID, name)

def removePassenger(passenger):
    del passenger

#gonna need an admin to monitor if driver or passenger got reported violating any rule or smth
class fuelType:
    def __init__(self, fuelType):
        self.fuelType = fuelType

        def getFuelType(self):
            return self.fuelType
        
        def setFuelType(self, fuelType):
            self.fuelType = fuelType
            fuelType = input("what type of fuel do you use? (RON95, RON97, Diesel) ").strip().upper()
            return fuelType
        

#fuel price will be a dropdown menu
class fuelPrice:
    def __init__(self, fuelPrice, fuelType):
        self.fuelprice = fuelPrice
        self.fuelType = fuelType

    def getFuelPrice(self):
        return self.price

    def setFuelPrice(self, price):
        self.price = price

    def calculateFuelPrice(self):
        if fuelType == "RON95":
            fuelType = "RON95"
            fuelPrice = float(2.05)
            return fuelType, fuelPrice
        elif fuelType == "RON97":
            fuelType = "RON97"
            fuelPrice = float(3.47)
            return fuelType, fuelPrice
        elif fuelType == "DIESEL":
            fuelType = "DIESEL"
            fuelPrice = float(3.25)
            return fuelType, fuelPrice
        else:
            return "Invalid input"
        return 0

#google api to take distance between 2 points
class Distance:
    def __init__(self, startP, endP):
        self.startP = startP
        self.endP = endP
        self.distance = None

    def calculate_distance(self):
        # Use Google Maps API or any other method to calculate the distance between startP and endP
        # Replace the following line with the actual implementation
        self.distance = 10.5  # Placeholder value for distance

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance
        distance = float(input("what is the distance between the 2 points? in km "))

class tank:
    def __init__(self, fuelType, fuelPrice, fuelUsed):
        self.fuelType = fuelType
        self.fuelPrice = fuelPrice
        self.fuelUsed = fuelUsed
        self.tank = None

    def setFuelUsed(self, fuelUsed):
        self.fuelUsed = fuelUsed
        fuelUsed=float(input("how much fuel in litre did you use? "))
        return fuelUsed

    def getFuelUsed(self):
        return self.fuelUsed

class noUser:
    def __init__(self, noUser):
        self.noUser = noUser

    def setNoUser(self, noUser):
        self.noUser = noUser
        noUser = int(input("how many people are in the car? "))
        return noUser

    def getNoUser(self):
        return self.noUser

#just assuming shit first before getting sort out
#google api only free  until week 13 after that need to pay up 15 nov || 13
def calculateFare(distance,fuelPrice,fuelUsed, noUser):
    fare = distance * fuelPrice * fuelUsed /noUser
    return fare


#testing only need to scrape this shit and rewrite
class Drive:
    def __init__(self, driver):
        self.driver = driver

    def start_drive(self):
        print(f"Starting drive with driver: {self.driver.name}")

# Testing the code
if __name__ == "__main__":
     
    drive.start_drive()