width = int(input())
height = int(input())
grid = [[i for i in input()] for _ in range(height)]

for row in range(height):#Row
    for column in range(width):#Column
        node = grid[row][column]
        #Find a power node
        if node == ".":
            continue
        ti = row+1
        tj = column+1
        #Increment until out of grid or found a power node
        while ti<height and grid[ti][column]!="0":
            ti+=1
        while tj<width and grid[row][tj]!="0":
            tj+=1
        #Print neighbor nodes (right and down).
        print(f"{column} {row} {tj if tj<width else -1} {row if tj<width else -1} {column if ti<height else -1} {ti if ti<height else -1}")
