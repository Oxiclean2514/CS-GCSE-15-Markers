# Initialize required variables, arrays and dictionaries
Prices = {
    "hatchback" : 535000,
    "saloon" : 495000,
    "estate" : 625000,
    "luxury seats" : 45000,
    "satellite" : 5500,
    "sensors" : 10000,
    "bluetooth" : 350,
    "sound" : 1000
}
newCarPrice = 0
tradeInPrice = 0
extrasPrice = 0
totalPrice = 0
Purchase = []

# Allow customers to choose a car to purchase
print("Please choose which car you would like to purchase:")
print("Type 1 for a Hatchback. Price: Rs 5.35 lakh")
print("Type 2 for a Saloon. Price: Rs 4.95 lakh")
print("Type 3 for an Estate. Price: Rs 6.25 lakh")
valid = False
# Checks input is a valid option
while valid != True:
    chosenCar = input()
    if chosenCar == ("1" or "2" or "3"):
        valid = True
    else:
        print("Invalid Input. Please try again.")
# Determines car price and adds car to array of what the customer has purchased
if chosenCar == "1":
    newCarPrice = Prices["hatchback"]
    Purchase.append("Hatchback")
elif chosenCar == "2":
    newCarPrice = Prices["saloon"]
    Purchase.append("Saloon")
elif chosenCar == "3":
    newCarPrice = Prices["estate"]
    Purchase.append("Estate")

# Allow customers to enter any optional extras
print("Please enter any optional extras you would like")
