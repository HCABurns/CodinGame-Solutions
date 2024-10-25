# Create Hashmap with item name : array of item costs.
items = {}
item_count = int(input())
customer_count = int(input())
for i in range(item_count):
    item = input().split()
    name = " ".join(item[:-1])
    cost = item[-1]
    if name not in items:
        items[name] = []
    items[name].append(cost)

# Check each customer request and print cheapest cost if found else NONE
for i in range(customer_count):
    item = input()
    min_cost = "X"
    # If item is valid then get minimum cost.
    if item in items:
        costs = items[item]  
        min_cost = min(costs)       
        # Remove item by setting to X
        items[item][costs.index(min_cost)] = "X"
    
    # Print correct result
    if min_cost != "X":
        print(min_cost) 
    else:
        print("NONE")
