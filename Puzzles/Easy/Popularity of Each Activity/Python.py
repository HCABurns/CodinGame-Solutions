# Get heigth of grid.
height = int(input())

# Get first row, get number of activities and attendees.
line1 = input().split(":")
grids_counter = len(line1)
scores = []
scores.append([i.count("*") for i in line1])
t = sum(scores[0])
quadrant = 0

# Go through grid and get attendees and store in correct position.
for i in range(height-1):
    row = input()
    # If splitter then add new score array and move on.
    if "+" in row:
        scores += [[0 for i in " "*grids_counter]]
        quadrant += 1
        continue
    
    # Get count for that activity and add to scores array.
    for j,activity in enumerate(row.split(":")):
        count =  activity.count("*")
        t += count
        scores[-1][j] += count

# Output the total attendees and percentages of attendees for each activity.
print(t,"attendees")
for row in scores:
    print(*[str(round(i/t*100)).rjust(3,"_")+"%" for i in row])
