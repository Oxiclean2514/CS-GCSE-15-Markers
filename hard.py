# Already initialized in question
Account = [[]]
AccDetails = [[]]
Size = 5

# Procedure to display balance
def viewBalance(AccountID):
    print("Your balance is: " + AccDetails[AccountID][1])

# Procedure to withdraw money
def withdrawMoney(AccountID):
    print("Please enter the amount of money you would like to withdraw")
    while True:
        valid = False
        if valid != True:
            try:
                withdrawAmount = float(input())
            except:
                print("Amount must be a number")
            else:
                valid = True
        overdraftLimit = AccDetails[AccountID][2]
        withdrawLimit = AccDetails[AccountID][3]
        if withdrawAmount > withdrawLimit:
            print("Error: Withdraw amount is above your withdraw limit")
        else:
            pass