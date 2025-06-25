from collections import defaultdict

# Functions to determine if inside shapes.
def inside_circle(x,y, radii):
    if (x**2 + y**2) <= radii**2:
        return True
    return False

def inside_diamond(x1,y1, corners, size):
    point_area = 0
    for (x2,y2),(x3,y3) in zip(corners, corners[1:]+[corners[0]]):
        point_area += 0.5 * abs(x1*(y2 - y3) + (x2*(y3 - y1)) + (x3*(y1 - y2)))
    if point_area == size**2*2:
        return True
    return False

def inside_square(x,y, size):
    if -size <= x <= size and -size <= y <= size:
        return True
    return False

# Form hashmap of players.
size = float(input()) / 2
corners = [[0,size],[size,0], [0,-size], [-size,0]]
n = int(input())
players = {input():0 for i in range(n)}

# Get points for a player based on throw.
t = int(input())
for i in range(t):
    name, *throw = input().split(" ")
    throw_x, throw_y =  map(int, throw)
    
    circle = inside_circle(throw_x, throw_y, size)
    diamond = inside_diamond(throw_x, throw_y, corners, size)
    square = inside_square(throw_x, throw_y, size)
    if diamond and circle:
        players[name] += 15
    elif circle:
        players[name] += 10
    elif square:
        players[name] += 5

# Output in descending order by score, and in order of appearance in case of a tie.
print(*[" ".join([str(j) for j in i]) for i in sorted(players.items(), key = lambda x:-x[1])],sep="\n")
