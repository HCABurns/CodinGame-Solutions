# Get the inputs.
a,b = input().split(",")
t1 = input().split(",")
t2 = input().split(",")

# Define scores and time leading. (Score in array to be updated in loop)
scores = {0:5,1:2,2:3,3:3}
score1 = [0]
score2 = [0]
leading_time_1 = 0
leading_time_2 = 0

# If a team scores, update their score and update time leading if possible.
time = 0
while time <= 80:
    for team,score in [(t1,score1),(t2,score2)]:
        for j,lst in enumerate(team):
            if not lst:continue
            for t in lst.split(" "):
                if int(t) == time:
                    score[0] += scores[j]
    
    if score1 > score2:
        leading_time_1 += 1

    if score2 > score1:
        leading_time_2 += 1
    time += 1

# Output the team, their score and minutes leading.
print(f"{a}: {score1[0]} {leading_time_1}")
print(f"{b}: {score2[0]} {leading_time_2}")
