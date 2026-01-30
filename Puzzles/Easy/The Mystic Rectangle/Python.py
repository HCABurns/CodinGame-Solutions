# Get inputs.
x, y = [int(i) for i in input().split()]
u, v = [int(i) for i in input().split()]

# Order inputs.
x1, x2 = min(x,u), max(x,u)
y1, y2 = min(y,v), max(y,v)

# Find minimum distance between horizontal and vertical.
d1 = min(x2-x1, (x2-x1) % 200, (x1-x2)%200) #E/W
d2 = min(y2-y1 , (y1-y2) % 150, ((y2-y1)%150)) #N/S

# Find time of travelling diagonal followed by horizontal and vertical respectively.
a = d1*0.5 + abs(d2-d1)*0.4
b = d2*0.5 + abs(d1-d2)*0.3

# Print the shortest time to reach the goal.
print(round(min(a,b),2))
