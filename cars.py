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
discounts = 0
totalPrice = 0
Purchase = []
repeatCustomer = False

# Allow customers to choose a car to purchase
print("Please choose which car you would like to purchase:")
print("Type 1 for a Hatchback. Price: Rs 5.35 lakh")
print("Type 2 for a Saloon. Price: Rs 4.95 lakh")
print("Type 3 for an Estate. Price: Rs 6.25 lakh")
valid = False
# Checks input is a valid option
while valid != True:
    chosenCar = input()
    if (chosenCar == "1") or (chosenCar == "2") or (chosenCar == "3"):
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

# Allow customers to enter any optional extras and loops until customer is finished
finished = False
print("Please enter any optional extras you would like")
while finished != True:
    print("Type 1 for a set of Luxury Seats. Price: Rs 45000")
    print("Type 2 for Satellite Navigation. Price: Rs 5500")
    print("Type 3 for Parking sensors. Price: Rs 10000")
    print("Type 4 for Bluetooth connectivity. Price: Rs 350")
    print("Type 5 for a sound system. Price: Rs 1000")
    print("Type 6 if you are done entering extras, or would not like to add any")
    chosenExtra = input()
    if chosenExtra == "1":
        extrasPrice = extrasPrice + Prices["luxury seats"]
        Purchase.append("Luxury Seats")
    elif chosenExtra == "2":
        extrasPrice = extrasPrice + Prices["satellite"]
        Purchase.append("Satellite Navigation")
    elif chosenExtra == "3":
        extrasPrice = extrasPrice + Prices["sensors"]
        Purchase.append("Parking Sensors")
    elif chosenExtra == "4":
        extrasPrice = extrasPrice + Prices["bluetooth"]
        Purchase.append("Bluetooth Connectivity")
    elif chosenExtra == "5":
        extrasPrice = extrasPrice + Prices["sound"]
        Purchase.append("Sound System")
    elif chosenExtra == "6":
        finished = True

# Allow customers to enter the price of their trade in
print("Did you trade in an old car? Please enter 1 if yes.")
if input() == "1":
    print("Please enter the offered price of your trade in,")
    valid = False
    while valid != True:
        tradeInPrice = input()
        try:
            tradeInPrice = float(tradeInPrice)
        except:
            print("Invalid Input, price must be a number. Please try again.")
        else:
            if (tradeInPrice >= 10000) and (tradeInPrice <= 100000):
                valid = True
            else:
                print("Invalid input, trade in price must be between Rs 10000 and Rs 100000. Please try again.")
else:
    None

# Determine whether customer is a repeat customer and qualifies for discounts
print("Are you a repeat customer? Please enter 1 for yes.")
if input() == "1":
    repeatCustomer = True
else:
    None

# Calculate final price and print receipt
totalPrice = newCarPrice + extrasPrice
print("Receipt:")
print("Car chosen: " + Purchase[0])
print("Extras Chosen:")
for i in range(1, len(Purchase)):
    print(Purchase[i] + ",")
print("Price of car and extras: Rs " + str(totalPrice))
if repeatCustomer == True:
    # Apply 10% discount on car before trade in and 10% off optional extras offered to repeat customers
    discounts = discounts + (newCarPrice * 0.1)
    discounts = discounts + (extrasPrice * 0.1)
    print("Repeat Customer discount: Rs " + str(discounts))
totalPrice = totalPrice - discounts
if tradeInPrice == 0:
    print("5% discount: " + str((totalPrice * 0.05)))
    totalPrice = totalPrice - (totalPrice * 0.05)
else:
    print("Trade in discount: " + tradeInPrice)
    totalPrice = totalPrice - tradeInPrice
print("Final price to pay: Rs " + str(totalPrice))

# Show available payment methods
print("Press any key to see the 3 available payment methods.")
input()
# Payment in full, 1% cashback
print("Payment method 1: Payment in full")
print("Total amount to pay: Rs " + str(totalPrice))
print("Number of payments: 1")
print("Cashback: Rs " + str(totalPrice * 0.01))
# Equal monthly payments over 4 years, no extra charge
print("\nPayment method 2: Monthly payment over 4 years")
print("Total amount to pay: Rs " + str(totalPrice))
print("Total number of payments: 48")
print("Price of each payment: " + str(totalPrice / 48))
# Equal monthly payments over 7 years, 5% charge
print("\nPayment method 3: Monthly payments over 7 years, total price is increased by 5%")
totalPrice = totalPrice * 1.05
print("Total amount to pay: " + str(totalPrice))
print("Total number of payments: 84")
print("Price of each payment: " + str(totalPrice / 84))
