#NOTE: All coordinates are in the form [y,x] or [row,column]
#Form grid from inputs and find coordinates of all "a" characters and store in array.
grid = []
starts = []
n = int(input())
grid = [input() for _ in range(n)]
for i,row in enumerate(grid):
    for j in range(len(row)):
        if row[j] == "a":
            starts.append((i,j))

def search(y,x,char):
    """
    Search function used for BFS searching grid for next character

    Parameters:
    int y - Row index to be searched
    int x - Column index to be seached
    String char - Character to be searched for. 

    Return:
    boolean - Boolean value indicating if Z has been found.
    """

    #Finishing condition - Z has been found return True
    if char == chr(ord("z")+1):
        return True
    
    #If an index is out of the grid, return False. 
    if y < 0 or y>=len(grid) or x<0 or x>=len(grid[0]):
        return False

    #Check if position has value of char.
    if grid[y][x] == char:
        #Set output array to char in correct position.
        out[y][x] = char
        next_char = chr(ord(char)+1)
        #Search in each direction from current position.
        v1 = search(y+1,x,next_char)
        v2 = search(y-1,x,next_char)
        v3 = search(y,x-1,next_char)
        v4 = search(y,x+1,next_char)
        #Check if Z has been found or not.
        if v1==v2==v3==v4==False:
            out[y][x] = "-"
            return False
        #If any search returns True then return True - Indicates search has resulted in Z being found
        return True
    return False

#Check all the start positions if they result in the correct sequence.
for y,x in starts:
    #Reset output
    out = [["-"]*len(grid[0]) for _ in range(n)]
    #Search starting with a character
    if search(y,x,"a"):
        print(*["".join(i) for i in out],sep="\n")
        break
