# Get width and height of input.
w, h = [int(i) for i in input().split()]

# Create output array
out = []

# Keep adding LSD onto out until it's length is 8. Then convert and print.
for i in range(h):
    for j in input().split():
        pixel = int(j)
        out.append(str(bin(pixel)[-1]))
        # If output is 8 bits, convert to ASCII char and print. Also clear array.
        if len(out) == 8:
            print(end=chr(int("".join(out),2)))
            out.clear()
