# Get ingredients.
e, f, s, b = [int(i) for i in input().split()]

# Calculate maxiumum of each type with given ingredients.
cookie = min(e//1, f//100, s//150, b//50)
cake= min(e//3, f//180, s//100, b//100)
muffin = min(e//2, f//150, s//100, b//150)
quantity = [cake,cookie, muffin]
types = ["Cake","Cookie","Muffin"] 

# Output the quantity and type.
print(max(quantity),types[quantity.index(max(quantity))])
