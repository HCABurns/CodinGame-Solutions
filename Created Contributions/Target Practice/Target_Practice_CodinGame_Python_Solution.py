def is_point_on_polygon(point, polygon):
    """
    Function for determining if point is on an edge of the polygon.
    """
    x, y = point
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]

        # Check if point lies on the line segment
        dx1 = x2 - x1
        dy1 = y2 - y1
        dx2 = x - x1
        dy2 = y - y1

        cross = dx1 * dy2 - dy1 * dx2
        if cross == 0:
            if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
                return True
    return False


def is_point_inside_polygon(point, polygon):
    """
    Determine if a point is inside a polygon using ray casting algorithm.
    
    point: (x, y) array.
    polygon: list of (x, y) array.

    Return True if point is inside the polygon, otherwise False.
    """
    x, y = point
    total = 0
    
    n = len(polygon)
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i + 1) % n]

        if (yi > y) != (yj > y):
            x_intersect = (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi
            if x < x_intersect:
                total += 1

    if total % 2 == 0:
        return is_point_on_polygon(point,polygon)
    else:
        return True

def is_point_in_circle(point, radius):
    x,y = point
    d1 = (x**2 + y**2)**0.5
    return d1 <= radius

# Read in the shapes and store.
shapes = {}
circles = []
N = int(input())
for i in range(N):
    score, corners = input().split(":")

    corners = corners.split(" ")
    arr = []

    for corner in corners:
        if "," not in corner:
            arr+=[float(corner)]
        else:
            x,y = map(float,corner.split(","))
            arr.append([x,y])

    shapes[i] = [int(score),arr]

# Read in the shots and store.
k = int(input())
shots = [[float(j) for j in input().split()] for _ in range(k)]

# Find the total points by getting the max points for each shot.
total_points = 0
for shot in shots:
    points = 0
    for i in range(N):
        # Determine if the shape is a circle or not and perform correct check.
        if len(shapes[i][1]) != 1:
            if is_point_inside_polygon(shot, shapes[i][1]):
                points = max(points, shapes[i][0])
        else:
            if is_point_in_circle(shot, shapes[i][1][0]):
                points = max(points, shapes[i][0])
    total_points += points

# Print the total points.
print(total_points)
