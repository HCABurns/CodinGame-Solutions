# Get the inputs.
l = int(input())
rooms = input()
n, k = [int(i) for i in input().split()]

# Assign the rooms and id.
rooms_ids = {char : i for i,char in enumerate(rooms) if char != "#"}

for i in range(n):
    # Get crewmate movements.
    crewmate = input()
    
    # Find the first room.
    pos = 0
    while pos < k and crewmate[pos] == "#":
        pos += 1
    
    # Ensure there is at least 1 valid room.
    if pos < k:
        current = crewmate[0]
    else:
        print("NOT SUS")
        continue

    # Define the current room, the position of the next room and the number of unknown movements.
    current = crewmate[pos]
    pos += 1
    unknown = 0

    # Check if each room is possible to reach within the given time, if not print SUS else NOT SUS.
    valid = False
    while pos < k:
        valid = False
        if crewmate[pos] == "#":
            unknown += 1
            pos+=1
            continue
        crid = rooms_ids[current]
        for j in range(-unknown-1,unknown+2):
            if rooms[(crid+j)%l] == crewmate[pos]:
                unknown = 0
                current = crewmate[pos]
                valid = True
                break
        pos += 1
        if not valid:
            break

    if valid or crewmate.count("#") >= len(crewmate)-1:
        print("NOT SUS")
    else:
        print("SUS")
