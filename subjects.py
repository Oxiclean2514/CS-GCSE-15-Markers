# Initializing required arrays and variables
Choices = []
Subjects = ["physics", "chemistry", "history", "geography", "computer science"]
Physics = 0
Chemistry = 0
History = 0
Geography = 0
Computer_Science = 0

# Allowing for input of data
for i in range(5):
    Valid = False
    print("Please enter student name")
    Name = input()
    while not Valid:
        print("Please enter first subject choice")
        First_Choice = input().lower()
        print("Please enter second subject choice")
        Second_Choice = input().lower()
        if (First_Choice and Second_Choice) in Subjects:
            Valid = True
        else:
            print("One of those subjects does not exist, please enter them again.")
    # Append name and choices to array
    Choices.append([Name, First_Choice, Second_Choice])
    # Update subject numbers
    for j in [First_Choice, Second_Choice]:
        if j == "physics":
            Physics = Physics + 1
        elif j == "chemistry":
            Chemistry = Chemistry + 1
        elif j == "history":
            History = History + 1
        elif j == "geography":
            Geography = Geography + 1
        elif j == "computer science":
            Computer_Science = Computer_Science + 1

print(Choices)
