# Get board and remove any noise.
pieces = input()
pieces += pieces.lower()
before = [[i if i in pieces else "." for i in input()] for _ in range(8)]
after = [[i if i in pieces else "." for i in input()] for _ in range(8)]

# Find which piece was moved and to where.
p1 = [0,0]
p2 = [0,0]
taken = False
for i in range(8):
    for j in range(8):

        if before[i][j] == after[i][j]:continue

        if before[i][j] not in pieces:
            p2 = [i,j]
        else:
            if after[i][j] not in pieces:
                p1 = [i,j]
            else:
                taken = True
                p2 = [i,j]

# Determine if a knight or not.
dy = abs(p1[0]-p2[0])
dx = abs(p1[1]-p2[1])
knight = (dy==1 and dx==2) or (dy==2 and dx==1)

# Print move and if it's a knight or other piece.
print(f"{chr(ord('a')+p1[1])}{8-p1[0]}{'-x'[taken]}{chr(ord('a')+p2[1])}{8-p2[0]}")
print(["Other","Knight"][knight])
