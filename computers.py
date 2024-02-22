# Import required modules
from random import randint
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
    "p5" : 12,
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
    order_numbers.append(orderNumber)
    return(orderNumber)
    
# Start main loop
while True == True:
    # Obtain user input of which components they want to buy
    print("Please choose a processor:")
    print("Type 1 for p3")
    print("Type 2 for p5")
    print("Type 3 for p7")
    choice = input()
    break
