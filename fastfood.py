# Initialize required arrays and variables
menuItems = ["French Fries", "1/4 pound burger", "1/4 pound cheeseburger", "1/2 pound burger", "1/2 pound cheeseburger", "Medium pizza", "Medium pizza with extra toppings", "Large pizza", "Large pizza with extra toppings", "Garlic bread"]
menuPrices = [2.0, 5.0, 5.55, 7.0, 7.5, 9.0, 11.0, 12.0, 14.5, 4.5]
menuCodes = ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10"]
menuSize = len(menuItems)
dailyTakings = 0
profit = 0
orderNumber = 1        
    
# Function for ordering
def order(): 
    orderItems = []
    orderQuantities = []
    orderPrice = 0
    # Print out full menu
    print("Menu:")
    for i in range(menuSize):
        print(menuItems[i] + " Price: $" + str(menuPrices[i]) + " Code: " + menuCodes[i])
    # Allow customers to enter item code and quantity until finished
    while finished != True:
        print("\nPlease enter first item code for your order, or \"finish\" if done ordering")
        choice = input()
        if choice == "finish":
            finished = True
        else:
            try:
                # Calculate array index of item user has chosen
                itemIndex = menuCodes.index(choice)
            except:
                print("Invalid code, please try again.")
            else:
                # Append array index of item user has chosen to orderItems array
                orderItems.append(itemIndex)
            valid = False
            while valid != True:
                # Allow user to choose quantity and validate input is integer
                print("Please enter quantity of item:")
                try:
                    quantity = int(input())
                except:
                    print("Invalid input, please enter a whole number")
                else:
                    orderQuantities.append(quantity)  
                    orderPrice = orderPrice+(menuPrices[itemIndex]*quantity)
                    valid = True

        # Generate unique order code and print full receipt


# Initialize main loop
while True:
    print("Enter 1 to place an order, 2 to calculate daily takings and profit or 3 to exit")
    choice = input()
    if choice == "1":
        order()
    elif choice == "2":
        pass
    elif choice == "3":
        exit()
    else:
        print("Invalid Input, please try again.")