# Already initialized in question
Account = [[]]
AccDetails = [[]]
Size = 5

# Procedure to display balance
def viewBalance(AccountID):
    print("Your balance is: " + AccDetails[AccountID][1])
    return()

# Procedure to withdraw money
def withdrawMoney(AccountID):
    print("Please enter the amount of money you would like to withdraw")
    while True:
        # Validation check confirming amount is a number
        valid = False
        while valid != True:
            try:
                withdrawAmount = float(input())
            except:
                print("Amount must be a number")
            else:
                valid = True
        currentBalance = AccDetails[AccountID][1]
        overdraftLimit = AccDetails[AccountID][2]
        withdrawLimit = AccDetails[AccountID][3]
        # Validation checks on whether withrawal is allowed to go through
        if withdrawAmount > withdrawLimit:
            print("Error: Withdraw amount is above your withdraw limit")
        elif (currentBalance-withdrawAmount) < overdraftLimit:
            print("Error: Withdrawing this amount would take you over your overdraft limit")
        else:
            # Process accepted withdrawal
            currentBalance = currentBalance-withdrawAmount
            AccDetails[AccountID][1] = currentBalance
            print("Money withdrawn successfully")
            return()

# Function to allow depositing money
def DepositMoney(AccountID):
    print("Please enter the amount of money to deposit")
    pass


print("Welcome to the banking system")
while True:
    # Allow user to enter Account ID, validate it is an integer
    print("Please enter your account ID:")
    valid = False
    while valid != True:
        try:
            accountID = int(input())
        except:
            print("Invalid account ID. Account ID must be a whole number")
        else:
            valid = True
    # Allow user to enter name and password
    print("Please enter the full name on your account")
    enteredName = input()
    print("Please enter your account password")
    enteredPassword = input()
    # Check that name and password match recorded values, if so login, else do not
    name = Account[accountID][1]
    password = Account[accountID][2]
    if (enteredName == name) and (password == enteredPassword):
        print("Login successful.")
        break
    else:
        print("Invalid details entered. Please try again.")

# Present logged in users with menu
while True:
    print("\nTo view your balance, please press 1")
    print("To withdraw money, please press 2")
    print("To deposit money, please press 3")
    print("To exit, please press 4")
    choice = input()
    if choice == "1":
        viewBalance(accountID)
    elif choice == "2":
        withdrawMoney(accountID)
    elif choice == "3":
        DepositMoney(accountID)
    elif choice == "4":
        exit()
    else:
        print("Invalid input. Please try again.")