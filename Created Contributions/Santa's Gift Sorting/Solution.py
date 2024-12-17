# Define order.
order = "metal, wooden, plastic, paper, electronic, glass".split(", ")

# Get gifts and create array.
gifts = []
n = int(input())
assert n<50,"N is larger than 50"
for i in range(n):
    name, type = input().split(",")
    assert len(name+type)+1 < 50, f"Input - {name+','+type} is larger than 50"  
    assert type in order, f"Type is not valid: {type}"
    gifts.append([type,name])

# Print gifts ordered based on type then name.
for _,gift in sorted(gifts, key = lambda gift : (order.index(gift[0]),gift[1])):
    print(gift)
