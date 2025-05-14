# Get input and form grid.
hi, wi = [int(i) for i in input().split()]
style = input()
how_many_triangles = int(input())
grid = [["*" for _ in range(wi)] for _ in range(hi)]

def area_finder(x_1,y_1, x_2, y_2, x_3, y_3):
    """
    Function to find the area between three points using shoelace determinant.
    """
    return abs(x_1*(y_2 - y_3) + x_2*(y_3 - y_1) + x_3*(y_1 - y_2))
    
# Complete the triangle toggles.
for i in range(how_many_triangles):
    x_1, y_1, x_2, y_2, x_3, y_3 = [int(j) for j in input().split()]
    min_x = min(x_1,x_2,x_3)
    max_x = max(x_1,x_2,x_3)
    min_y = min(y_1,y_2,y_3)
    max_y = max(y_1,y_2,y_3)
    for ii in range(min_y,max_y+1):
        for jj in range(min_x,max_x+1): 
            # Find area from point to two others, check the area matches the triangles.
            # If it does, the point is inside the triangle.
            a1 = area_finder(jj,ii, x_1, y_1, x_2, y_2)
            a2 = area_finder(jj,ii, x_1, y_1, x_3, y_3)
            a3 = area_finder(jj,ii, x_2, y_2, x_3, y_3)
            a = area_finder(x_1, y_1, x_2, y_2, x_3, y_3)
            if a == a1 + a2 + a3 and 0<=ii<hi and 0<=jj<wi:
                grid[ii][jj] = [" ","*"][grid[ii][jj] == " "]

# Output the grid.
for row in grid:
    if style == "expanded":
        print(" ".join(row))
    else:
        print("".join(row))
