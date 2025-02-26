# Get the border design and width and height of the picture to be framed.
border = input()
h, w = [int(i) for i in input().split()]

# Print top border of the frame
for i in range(1,len(border)+1):
    print(border[:i] + border[i-1]*(w+2+(len(border)-i)*2) + border[:i][::-1])
print(border + " "*(w+2) + border[::-1])

# Print picture with border.
for i in range(h):
    line = input()  # the ASCII art picture line by line
    print(border+" "+line+" "+border[::-1])

# Print the bottom of the frame.
print(border + " "*(w+2) + border[::-1])
for i in range(len(border),0,-1):
    print(border[:i] + border[i-1]*(w+2+(len(border)-i)*2) + border[:i][::-1])
