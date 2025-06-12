# Form snails and the order.
snails = {}
order = []
number_snails = int(input())
for i in range(1,number_snails+1):
    speed_snail = int(input())
    snails[i] = [speed_snail, []]
    order += [i]

# Find end points and snail positions.
map_height = int(input())
map_width = int(input())
ends = []
for i in range(map_height):
    row = input()
    for j,char in enumerate(row):
        if char == "#":
            ends += [[i,j]]
        if char.isnumeric():
            snails[int(char)] = [snails[int(char)][0], [i,j]]

while True:
    # Move each character by their movement allowance until an end is found.
    for char in order:
        # Find the closest end by manhattan disance.
        speed, pos = snails[char]
        closest = [[0,0],999999]
        for goal in ends:
            i1, j1 = goal
            dist = abs(pos[0]- i1) + abs(pos[1] - j1)
            if dist < closest[1]:
                closest = [goal, dist]
        goal = closest[0]
        
        # Move snail by speed.
        for x in range(speed):
            if goal[0] != pos[0]:
                if goal[0] < pos[0]:
                    pos[0] -= 1
                elif goal[0] > pos[0]:
                    pos[0] += 1
            elif goal[1] != pos[1]:
                if goal[1] < pos[1]:
                    pos[1] -= 1
                elif goal[1] > pos[1]:
                    pos[1] += 1
            
            # If at goal then print.
            if goal == pos:
                print(char)
                quit()
        snails[char] = [speed, pos]
