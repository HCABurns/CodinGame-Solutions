# Get length and size of contents page.
lengthofline = int(input())
n = int(input())

# Array of 
counts = [0]

for i in range(n):
    # Get title, page number and indent amount.
    name, page = input().split(" ")
    indent = name.count(">")

    # Increment counter for directory/subdirectory.
    if len(counts) <= indent:
        counts += [1]
    else:
        counts[indent] += 1

        # Reset subdirectory counts.
        tmp = indent+1
        while tmp < len(counts):
            counts[tmp] = 0
            tmp += 1
    
    # Print contents line.
    print(("    "*indent + "" + str(counts[indent]) +" "+ name[indent:]).ljust(lengthofline - len(page),".") + page)
