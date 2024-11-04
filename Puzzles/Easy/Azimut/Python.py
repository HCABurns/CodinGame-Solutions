# Get Hashmap of angles and directions.
angles = {"N":0,"NE":45,"E":90,"SE":135,"S":180,"SW":225,"W":270,"NW":315}
directions = {"RIGHT":45,"LEFT":-45,"FORWARD":0,"BACK":180}

# Get starting direction.
start_direction = input()
direction = angles[start_direction]

# Simulate moves.
n = int(input())
for i in range(n):
    direction = (direction+directions[input()])%360

# Output the angle the person is facing.
for key,angle in angles.items():
    if angle == direction:  
        print(key)
        break
