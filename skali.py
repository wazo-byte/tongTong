import googlemaps 

# API KEY
API_KEY = ''

# Initialize the Google Maps client
gmaps = googlemaps.Client(key=API_KEY)

# Initialize the startingPoint and endPoint
origin = 'Taman Shamelin Sky Residency, Kuala Lumpur, Malaysia'
destination = 'Bukit Bintang, Kuala Lumpur, Malaysia'

# Get distance matrix from the API
klicks = gmaps.distance_matrix(origins=origin, destinations=destination, mode='driving')

# Extract the distance from the API and convert from meters to kilometers
klicks_m = klicks['rows'][0]['elements'][0]['distance']['value']
klicks_km = klicks_m / 1000

#return fuel eff in km/l based on car type from review of users
def getfuelEfficiency(carType):
    if carType == 'saga':
        return  14
    elif carType == 'axia':
        return 14
    elif carType == 'myvi':
        return  14
    elif carType == 'bezza':
        return  13
    else:
        raise ValueError("Invalid input") 

#param:
#distance_km(float): distance in km for trips
#fuelPrice(float): price per litre of fuel
#fuelEfficiency(float): fuel efficiency in km per litre
#noUser(int): number of users (passengers)


def calculateFare(distance_km, fuelPrice, fuelEfficiency, noUser):
    # Calculate total fuel used
    fuel_used = distance_km / fuelEfficiency
    # Calculate total fare 
    total_fare = fuel_used * fuelPrice
    # Calculate fare per user
    fare_per_user = total_fare / noUser
    return fare_per_user

# Test the fare calculation with example values
if __name__ == "__main__":
    # Example values
    fuelPrice = 2.05  # Price per litre for RON95
    noUser = 4  # Number of users (passengers)
    carType = 'saga'

try:
    fuelEfficiency = getfuelEfficiency(carType)
    fare = calculateFare(klicks_km, fuelPrice, fuelEfficiency, noUser)
    print(f"The calculated fare is: MYR {fare:.2f}"f"for each {noUser} passengers riding "f"{carType}\n from {origin} to {destination}."f" The distance is {klicks_km:.2f} km.")
except Exception as e:
    print(e)
