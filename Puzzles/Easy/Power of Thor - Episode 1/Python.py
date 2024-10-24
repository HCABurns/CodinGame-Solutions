# Get inputs
light_x,light_y,thor_x,thor_y=map(int,input().split())

# Loop and if thor needs to move a direction, append it to output.
while True:
    output=""
    # If thor is below light, move north.
    if light_y < thor_y:
        output="N"
        thor_y-=1
    # If thor is above light, move south.
    if light_y > thor_y:
        output="S"
        thor_y+=1
    # If thor is right of the light, move west.
    if light_x < thor_x:
        output+="W"
        thor_x+=1
    # If thor is left of the light, move east.
    if light_x > thor_x:
        output+="E"
        thor_x-=1
    
    # Print direction to travel
    print(output)
