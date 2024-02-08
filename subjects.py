# Initializing required arrays and variables
Choices = []
Subjects = ["physics", "chemistry", "history", "geography", "computer science"]
Subject_Numbers = [0, 0, 0, 0, 0]
Subject_Groups = []
Physics = []
Chemistry = []
History = []
Geography = []
Computer_Science = []
Unallocated = []
maxGroupSize = 5
minGroupSize = 2
numberOfStudents = 10
Spare_Places = []

# Allowing for input of data
for i in range(numberOfStudents):
    Valid = False
    print("Please enter student name")
    Name = input()
    while not Valid:
        # Check validity of subjects and that they are not both the same
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
    # Update subject numbers and add student names to appropriate subject array
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

# Print number of students for each subject
for h in range(5):
    print(str(Subject_Numbers[h]) + " Students have chosen " + Subjects[h])

# Identify over and under subscribed subjects by checking subject numbers array
for i in range(5):
    if Subject_Numbers[i] > (2*maxGroupSize):
        print(Subjects[i] + " is oversubscribed and some students have been unallocated.")
    elif Subject_Numbers[i] < (minGroupSize):
        print(Subjects[i] + " is undersubscribed and is not available this year.")

# Iterate through arrays containing student names for each subject
for currentSubject in [Physics, Chemistry, History, Geography, Computer_Science]:
    # If not enough students signed up, add all students to unallocated array and clear the subject array
    if len(currentSubject) < minGroupSize:
        Unallocated = Unallocated.extend(currentSubject)
        currentSubject.clear()
        currentSubject.append("Unavailable")
    # If too many students signed up, remove last name from subject array and add to unallocated
    # array until number of students is acceptable.
    while len(currentSubject) > (2*maxGroupSize):
        Unallocated.append(len(currentSubject)-1)
        currentSubject.pop(len(currentSubject)-1)
# Print list of students names for each subject
Student_Groups = [Physics, Chemistry, History, Geography, Computer_Science]
for j in range(5):
    # Prints out lists for seperate groups if more than 20 students are doing the subject
    if len(Student_Groups[j]) > 20:
        print(Subjects[j] + ":")
        Students = ', '.join(Student_Groups[j][0:19])
        print("Group 1: " + Students)
        Students = ', '.join(Student_Groups[j][20:(len(Student_Groups[j])-1)])
        print("Group 2: " + Students)
    else:
        print(Subjects[j] + ":")
        Students = ', '.join(Student_Groups[j])
        print("Group 1: " + Students)
# Prints unallocated students
Students = ', '.join(Unallocated)
print("Unallocated Students: " + Students)

# Calculates spare places and places into an array
def calculateSparePlaces(Subject):
    if len(Subject) > 20:
        sparePlaces = 40 - len(Subject)
    else:
        sparePlaces = 20 - len(Subject)
    return sparePlaces
Spare_Places[0] = calculateSparePlaces(Physics)
Spare_Places[1] = calculateSparePlaces(Chemistry)
Spare_Places[2] = calculateSparePlaces(History)
Spare_Places[3] = calculateSparePlaces(Geography)
Spare_Places[4] = calculateSparePlaces(Computer_Science)

# Prints spare places for each subject and calculates total
totalSparePlaces = 0
print("Spare Places:")
for h in range(5):
    print(Subjects[h] + ": " + str(Spare_Places[h]))
    totalSparePlaces = totalSparePlaces + Spare_Places[h]
print("Total spare places: " + str(totalSparePlaces))
print("Total unallocated places: " + str(len(Unallocated)))
# Works out whether spare places can cover unallocated places
if totalSparePlaces > len(Unallocated):
    print("There are enough spare places to cover the unallocated students")
else:
    print("There are not enough spare places to cover the unallocated students")

    
