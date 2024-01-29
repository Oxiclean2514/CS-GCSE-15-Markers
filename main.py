# Initializing required arrays and variables
Students = []
NumberOfChoices = []
Choices = []
StudentEntryIndex = 0
# Initializing dictionary to store choices and number of Students
Subjects = {
    "Physics": 0,
    "Chemistry": 0,
    "History": 0,
    "Geography":  0,
    "Computer Science": 0,
}

# Allow user to input student name and choices 
for i in range(60):
    print("Enter Student name")
    Students.append(input())
    print("Enter student's choices. Enter \"None\" if they didn't choose any extra subjects.")
    StudentChoices = input().lower()
    if StudentChoices == "none":
        print("None")
        NumberOfChoices.append(0)
        continue
