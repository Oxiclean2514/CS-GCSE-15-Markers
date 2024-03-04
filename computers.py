# computers.py
# Written by Luca B
# Import required modules
from random import randint
from datetime import date
# Initialize required dictionaries, arrays and variables
component_prices = {
    "p3" : 100,
    "p5" : 120,
    "p7" : 200,
    "16GB" : 75,
    "32GB" : 150,
    "1TB" : 50,
    "2TB" : 100,
    "19\"" : 65,
    "23\"" : 120,
    "Mini Tower" : 40,
    "Midi Tower" : 70,
    "2 ports" : 10,
    "4 ports" : 20,
}
component_stock = {
    "p3" : 10,
    "p5" : 10,
    "p7" : 10,
    "16GB" : 10,
    "32GB" : 10,
    "1TB" : 10,
    "2TB" : 10,
    "19\"" : 10,
    "23\"" : 10,
    "Mini Tower" : 10,
    "Midi Tower" : 10,
    "2 ports" : 10,
    "4 ports" : 10,
}
components = []
order_numbers = []
computerPrice = 0

# Define function to generate a random, unique, 5 digit order number
def generate_order_number():
    valid = False
    while valid != True:
        orderNumber = str(randint(10000, 99999))
        present = False
        for i in range(len(order_numbers)):
            if orderNumber == order_numbers[i]:
                present = True
        if present == False:
            valid = True
    return(orderNumber)
    
# Start main loop
while True == True:
    # Obtain user input of which components they want to buy - code repeated for each component 
    valid = False
    while valid != True:
        print("Please choose a processor:")
        print("Type 1 for p3")
        print("Type 2 for p5")
        print("Type 3 for p7")
        choice = input()
        if choice == "1":
            components.append("p3")
            computerPrice = computerPrice + component_prices["p3"]
            valid = True
        elif choice == "2":
            components.append("p5")
            computerPrice = computerPrice + component_prices["p5"]
            valid = True
        elif choice == "3":
            components.append("p7")
            computerPrice = computerPrice + component_prices["p7"]
            valid = True
        else:
            print("Invalid input. Please try again.")
    valid = False
    while valid != True:
        print("Please choose a RAM option:")
        print("Type 1 for 16GB")
        print("Type 2 for 32GB")
        choice = input()
        if choice == "1":
            components.append("16GB")
            computerPrice = computerPrice + component_prices["16GB"]
            valid = True
        elif choice == "2":
            components.append("32GB")
            computerPrice = computerPrice + component_prices["32GB"]
            valid = True
        else:
            print("Invalid input. Please try again.")
    valid = False
    while valid != True:
        print("Please choose a RAM option:")
        print("Type 1 for 16GB")
        print("Type 2 for 32GB")
        choice = input()
        if choice == "1":
            components.append("16GB")
            computerPrice = computerPrice + component_prices["16GB"]
            valid = True
        elif choice == "2":
            components.append("32GB")
            computerPrice = computerPrice + component_prices["32GB"]
            valid = True
        else:
            print("Invalid input. Please try again.")
    valid = False
    while valid != True:
        print("Please choose a Storage option:")
        print("Type 1 for 1TB")
        print("Type 2 for 2TB")
        choice = input()
        if choice == "1":
            components.append("1TB")
            computerPrice = computerPrice + component_prices["1TB"]
            valid = True
        elif choice == "2":
            components.append("2TB")
            computerPrice = computerPrice + component_prices["2TB"]
            valid = True
        else:
            print("Invalid input. Please try again.")
    valid = False
    while valid != True:
        print("Please choose a screen size:")
        print("Type 1 for 19\"")
        print("Type 2 for 23\"")
        choice = input()
        if choice == "1":
            components.append("19\"")
            computerPrice = computerPrice + component_prices["19\""]
            valid = True
        elif choice == "2":
            components.append("23\"")
            computerPrice = computerPrice + component_prices["23\""]
            valid = True
        else:
            print("Invalid input. Please try again.")
    valid = False
    while valid != True:
        print("Please choose a case size:")
        print("Type 1 for a Mini Tower")
        print("Type 2 for a Midi Tower")
        choice = input()
        if choice == "1":
            components.append("Mini Tower")
            computerPrice = computerPrice + component_prices["Mini Tower"]
            valid = True
        elif choice == "2":
            components.append("Midi Tower")
            computerPrice = computerPrice + component_prices["Midi Tower"]
            valid = True
        else:
            print("Invalid input. Please try again.")
    valid = False
    while valid != True:
        print("Please choose a number of USB ports:")
        print("Type 1 for 2 ports")
        print("Type 2 for 4 ports")
        choice = input()
        if choice == "1":
            components.append("2 ports")
            computerPrice = computerPrice + component_prices["2 ports"]
            valid = True
        elif choice == "2":
            components.append("4 ports")
            computerPrice = computerPrice + component_prices["4 ports"]
            valid = True
        else:
            print("Invalid input. Please try again.")
    
    # Generate estimate
    tempEstimateNumber = generate_order_number()
    print("Estimate Number: " + tempEstimateNumber)
    print("Components:")
    for i in range(len(components)):
        print(components[i] + ": $" + str(component_prices[components[i]]))
        computerPrice = computerPrice+component_prices[components[i]]
    print("Service Charge (20%): " + str(computerPrice*0.2))
    computerPrice = computerPrice + (computerPrice*2)
    print("Total Price: " + str(computerPrice))
    print("Please enter 1 to place this order or anything else to cancel")
    choice = input()
    if choice == "1":
        inStock = True
        for i in range(len(components)):
            if component_stock[components[i]] <= 0:
                inStock = False
        if inStock != True:
            print("One or more components are not in stock. Please try again with different components.")
            print("Press any key to return to menu")
            input()
        else:
            for j in range(len(components)):
                with component_stock[components[j]] as comp:
                    comp = comp-1
            order_numbers.append(tempEstimateNumber)
            # Need to print the customer+shop copy final receipt
