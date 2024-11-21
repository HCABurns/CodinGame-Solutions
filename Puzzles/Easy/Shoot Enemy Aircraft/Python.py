# Get planes locations and position of SAM launcher.
pos = []
planes = []
n = int(input())
for i in range(n):
    line = input()
    for j,char in enumerate(line):
        if char in "<>":
            planes.append([i,j])
        if char == "^":
            pos = [i+1 , j]#NOTE:+1 As missle travels from launcher location.

# Continue until all planes have been shot down.
while len(planes) > 0:
    # Define boolean if a shot is to be taken or not.
    shoot = False

    # Plane to be remove
    to_remove = None

    # Move plane and check if they can be shot.
    for i , plane in enumerate(planes):
        y , x = plane
        # Check if vertical distance between plane and SAM equals horizontal distance between.
        # If so then they will intercept so shoot.
        if abs(x-pos[1]) == pos[0] - y:
            to_remove = plane
            shoot = True
        else:
            # Move plane.
            if x < pos[1]:
                plane[1] += 1
            else:
                plane[1] -= 1
    
    # Remove plane if shot.
    if to_remove:planes.remove(to_remove)
    
    # Output if a shot has been taken or not.
    if shoot:
        print("SHOOT")
    else:
        print("WAIT")
