# Get required inputs.
*_,exit_y,exit_x,_,_,n=[int(i)for i in input().split()]

# Sort elevators locations.
elevators=sorted([[int(j) for j in input().split()]for _ in range(n)])

while True:
    # Get required inputs
    clone_floor, clone_pos, direction = input().split()
    clone_floor,clone_pos = int(clone_floor), int(clone_pos)
    direction=direction[0] 

    # If not on the exit floor, set the loction the the elevator on the current level.
    if clone_floor!=-1 and clone_floor != exit_y:
        elevator_location=elevators[clone_floor]
    # On exit floor so set location to the exit.
    else:
        elevator_location=(exit_y,exit_x)
    
    # If bot is heading the wrong direction for their elevator/exit, make them block.
    if clone_pos<elevator_location[1]and direction=="L"or clone_pos>elevator_location[1]and direction=="R":
        print("BLOCK")
    else:
        print("WAIT")
