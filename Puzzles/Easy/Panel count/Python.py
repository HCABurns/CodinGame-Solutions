# Define empty array of people.
people = []

# Get property list.
properties = [input() for i in range(int(input()))]

# Form hahsmaps of people containing properties and value.
n = int(input())
for i in range(n):
    name , *info = input().split()
    people.append({})
    for prop, data in zip(properties,info):
        people[-1][prop] = data

# Get criteria to be used searched.
criteria = [input() for i in range(int(input()))]

# Search every person against the criteria and print number of people who satisfy the criteria.
for formula in criteria:
    total = 0
    for info in people:
        valid = True
        for data in formula.split("AND"):
            prop , val = data.strip().split("=")
            if info.get(prop,None) != val:
                valid = False
                break
        if valid:
            total += 1
    print(total)
