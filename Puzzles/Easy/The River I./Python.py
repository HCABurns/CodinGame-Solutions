# Get inputs.
r_1 = int(input())
r_2 = int(input())

# Ensure r_1 is the smaller value.
r_1 , r_2 = min(r_1,r_2) , max(r_1,r_2)

# Continue until equal values.
while r_1 != r_2:
    
    # Compute algorithm until r_1 is larger or equal to r_2.
    while r_1 < r_2:
        r_1 += sum([int(i) for i in str(r_1)])

    # If r_2 is smaller than r_1, compute the next value.
    if r_2<r_1:
        r_2 += sum([int(i) for i in str(r_2)])

# Output the meeting point.
print(r_1)
