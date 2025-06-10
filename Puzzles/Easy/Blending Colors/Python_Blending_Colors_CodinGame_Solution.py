import math

# Define Classes for the shapes.
class shape:
    def __init__(self, c1, c2, size, colour):
        self.x1 = float(c1)
        self.y1 = float(c2)
        self.size = float(size)
        self.colour = colour
    def get_colour(self):
        return self.colour

class square(shape):
    def inside(self, x, y):
        # Inside y
        if (self.y1 < y < self.y1+self.size) and (self.x1 < x < self.x1+self.size):
            return self.colour
        if (self.x1 == x and self.y1 <= y <= self.y1+self.size) or (self.x1+self.size == x and self.y1 <= y <= self.y1+self.size) or (self.y1 == y and self.x1 <= x <= self.x1+self.size) or (self.y1+self.size== y and self.x1 <= x <= self.x1+self.size):
            return [0,0,0]
        return [255,255,255]

class circle(shape):
    def inside(self, x, y):
        if ((self.x1-x)**2 + (self.y1-y)**2)**0.5 < self.size:
            return self.colour
        if ((self.x1-x)**2 + (self.y1-y)**2) == self.size**2:
            return [0,0,0]
        return [255,255,255]

def round(value):
    """
    Custom function to round 0.5 up. (Pythons bankers rounding is 0.5 goes down.)
    """
    frac = value - math.floor(value)
    value = math.floor(value) if frac < 0.5 else math.ceil(value) 
    return value

# Form array of shapes.
s, p = [int(i) for i in input().split()]
shapes = []
for i in range(s):
    t, *values = input().split()
    x,y, size, r,g,b = map(int, values)
    if t == "SQUARE":
        shapes += [square(x,y,size, [r,g,b])]
    else:
        shapes += [circle(x,y,size, [r,g,b])]

# Find and print the blended colour, border color or white.
for i in range(p):
    x, y = [int(j) for j in input().split()]
    colours = []
    for shape in shapes:
        values = shape.inside(x,y)
        if values != [255,255,255]:
            colours += [values]

    # Print, white, black or belnded colour.
    if len(colours) == 0:
        print("(255, 255, 255)")
    elif [0,0,0] in colours:
        print("(0, 0, 0)")
    else:
        r = round(sum([i[0] for i in colours])/len(colours))
        g = round(sum([i[1] for i in colours])/len(colours))
        b = round(sum([i[2] for i in colours])/len(colours))
        print(f"({r}, {g}, {b})")
