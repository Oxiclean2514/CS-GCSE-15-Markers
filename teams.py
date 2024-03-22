# Already initialized in question
LeagueSize = 5
MatchNo = 5
TeamName = []
TeamPoints = [[]] # Il populate these when i can be bothered

# Initialize required variables and arrays
TotalPoints = []
AwayWins = []
HomeWins = []
Draws = []
Losses = []

# Iterate through each team and their matches

for i in range(LeagueSize):
    Total = 0
    AwayCount = 0
    HomeCount = 0
    DrawCount = 0
    LossCount = 0
    for j in range(MatchNo)
    # Take current match points, check outcome of game using number of points and add to arrays
    temp = TeamPoints[i][j]
    Total = Total+temp
    if temp == 0:
        LossCount = LossCount+1
    elif temp == 1:
        DrawCount = DrawCount+1
    elif temp == 2:
        HomeCount = HomeCount+1
    elif temp == 3:
        AwayCount = AwayCount+1
    # Append total point sand Match Statistics to relevant arrays
    TotalPoints.append(Total)
    AwayWins.append(AwayCount)
    HomeWins.append(HomeCount)
    Draws.append(DrawCount)
    Losses.append(LossCount)

# Output required information for a each team
for i in range(LeagueSize):
    print("Team Name: " + TeamName[i])
    print("Total Points: " + str(TotalPoints[i]))
    print("Away wins: " + str(AwayWins[i]))
    print("Home wins: " + str(HomeWins[i]))
    print("Draws: " + str(Draws[i]))
    print("Losses: " + str(Losses[i]))

# Find out and store index for team with Lowest and Highest score
LowestIndex = TotalPoints.index(min(TotalPoints))
HighestIndex = TotalPoints.index(max(TotalPoints))

# Print team with lowest and highest score
print("Team with lowest score: " + TeamName[LowestIndex])
print("Team with highest score: " + TeamName[HighestIndex])