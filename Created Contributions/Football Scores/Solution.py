# Get number of results
n = int(input())

# Map for storing teams and points
teams_map = {}
for i in range(n):
    result = input()

    # Split the result
    teams , score = result.split(":")
    team1 , team2 = teams.split(" vs. ")
    score1 , score2 = score.split("-")

    # Add to map if not already in it
    if team1 not in teams_map:
        teams_map[team1] = 0
    if team2 not in teams_map:
        teams_map[team2] = 0

    # Add correct points
    if score1 > score2:
        teams_map[team1] += 3
    elif score2 > score1:
        teams_map[team2] += 3
    else:
        teams_map[team1] += 1
        teams_map[team2] += 1

# Sort by decreasing score and increasing alphabetical order for the team names.
teams = list(teams_map.items())
teams.sort(key = lambda x : (-x[1] , x[0]) )

for name,_ in teams:
    print(name)
