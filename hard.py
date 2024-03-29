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
        currentBalance = AccDetails[AccountID][1]
        overdraftLimit = AccDetails[AccountID][2]
        withdrawLimit = AccDetails[AccountID][3]
        if withdrawAmount > withdrawLimit:
            print("Error: Withdraw amount is above your withdraw limit")
        elif (currentBalance-withdrawAmount) < overdraftLimit:
            print("Error: Withdrawing this amount would take you over your overdraft limit")
        else:
            currentBalance = currentBalance-withdrawAmount
            AccDetails[AccountID][1] = currentBalance
            print("Money withdrawn successfully")

def DepositMoney(AccountID):
    pass


print("Welcome to the banking system")
while True:
    pass     