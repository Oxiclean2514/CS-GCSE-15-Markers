# Initializing required arrays and variables
Choices = []
Subjects = ["physics", "chemistry", "history", "geography", "computer science"]
Subject_Numbers = [0, 0, 0, 0, 0]
Physics = []
Chemistry = []
History = []
Geography = []
Computer_Science = []


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
            if First_Choice != Second_Choice:
                Valid = True
            else:
                print("Both subjects cannot be the same, please enter them again.")
        else:
            print("One of those subjects does not exist, please enter them again.")
    # Append name and choices to array
    Choices.append([Name, First_Choice, Second_Choice])
    # Update subject numbers
    for j in [First_Choice, Second_Choice]:
        if j == "physics":
            Subject_Numbers[0] = Subject_Numbers[0] + 1
            Physics.append(Name)
        elif j == "chemistry":
            Subject_Numbers[1] = Subject_Numbers[1] + 1
            Chemistry.append(Name)
        elif j == "history":
            Subject_Numbers[2] = Subject_Numbers[2] + 1
            History.append(Name)
        elif j == "geography":
            Subject_Numbers[3] = Subject_Numbers[3] + 1
            Geography.append(Name)
        elif j == "computer science":
            Subject_Numbers[4] = Subject_Numbers[4] + 1
            Computer_Science.append(Name)

for h in range(5):
    print(str(Subject_Numbers[h]) + " Students have chosen " + Subjects[h])

