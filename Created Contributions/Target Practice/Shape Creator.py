import matplotlib.pyplot as plt

def plot_shape(coords, point):
    """
    Takes a list of (x, y) tuples representing shape corners
    and plots the filled shape.
    """
    # Unpack x and y coordinates
    x_vals, y_vals = zip(*coords)

    # Plot filled polygon
    plt.fill(x_vals, y_vals, edgecolor='black', fill=True, facecolor='skyblue', linewidth=2)

    # Optionally plot corner points
    plt.plot(x_vals, y_vals, 'o', color='black')

    plt.plot(point[0],point[1], "o", color = "red")

    # Equal scaling and grid for clarity
    plt.axis('equal')
    plt.grid(True)
    plt.title("Filled Shape")
    plt.show()


def plot_shapes(polygons, point, colors=None):
    """
    Plots multiple filled polygons without overwriting overlaps.

    polygons: list of lists of (x, y) points
    colors: optional list of facecolors for each polygon
    """
    plt.figure()
    
    for i, poly in enumerate(polygons):
        x_vals, y_vals = zip(*poly)
        
        # Cycle through colors or default to semi-transparent fill
        facecolor = colors[i] if colors and i < len(colors) else f"C{i % 10}"
        
        plt.fill(x_vals, y_vals, edgecolor='black', linewidth=2,
                 facecolor=facecolor, alpha=0.5)

    plt.plot(point[0],point[1], "o", color = "red")
    plt.axis('equal')
    plt.grid(True)
    plt.title("Multiple Polygons with Transparency")
    plt.show()

def is_point_inside_polygon(point, polygon):
    x, y = point
    inside = False

    n = len(polygon)
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i + 1) % n]

        if (yi > y) != (yj > y):
            x_intersect = (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi
            if x < x_intersect:
                inside = not inside

    return inside




# Example: triangle (x,y)
shape = [
    (0, 0),
    (0,20),
    (5,20),
    (3,10),
    (10, 10),
    (20, 0),
    (10,5),
    (0, 0)  # Close the shape
]

point = (17,1)

polygon1 = [(0, 0), (0, 20), (5, 20), (3, 10), (10, 10), (20, 0), (0, 0)]
polygon2 = [(-30, -30), (-30, 30), (30, 30), (30, -30), (-30,-30)]

shapes = [polygon1,polygon2]
plot_shapes(shapes, point)# None, point)

for shape in shapes:
 print(is_point_inside_polygon(point, shape))
#plot_shape(shape, point)
