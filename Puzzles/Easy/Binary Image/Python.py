# Read in size
h = int(input())

# Define charaters, array for storing rows and length of row.
chars = ".O"
rows = []
rows_length = -1

# Check all rows are the same length and store.
for i in range(h):
    row = input().split()
    sum_val = sum([int(i) for i in row])
    if rows_length == -1:
        rows_length = sum_val
    if rows_length != sum_val:
        break
    rows += [row]

# If all rows have been read in, convert to text and print. Otherwise, print invalid.
if len(rows) == h:
    for row in rows:
        out = []
        for i,size in enumerate(row):
            out += [chars[i%2]*int(size)]
        print("".join(out))
else:
    print("INVALID")
