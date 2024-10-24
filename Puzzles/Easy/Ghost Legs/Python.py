# Get height and width of the grid.
h=int(input().split()[1])

# Get starting characters and store in array.
chars=[i for i in input() if i != " "]

for i in range(h-2): # -2 as first and last column is ignored for this phase.

    # Get input row.
    line = input()
    
    # Get starting positions.
    if i==0:grid=[j for j,c in enumerate(line) if c=="|"]

    # Iterate over the grid, row by row, checking for steps to move over columns.
    for j,column in enumerate(grid):
        # Check  if moving right - If so, shift to next column
        if column!=len(line)-1 and line[column+1]=="-":
            grid[j]+=3
        # Check if moving left - If so, shift to previous column
        elif column!=0 and line[column-1]=="-":
            grid[j]-=3

# Output starting charater with ending position character. 
end = input().split()
for i,j in enumerate(chars):
    print(str(chars[i])+str(end[grid[i]//3]))
