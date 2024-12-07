# Arrays for position and points.
points = [25,18,15,12,10,8,6,4,2,1]
drivers = []

n = int(input())
for _ in range(n):
    # Split name and results.
    name,results = input().split(":")
    
    # Drivers points total.
    total = 0
    for i in results.split(" "):
        # Get position in race.
        res = "".join([j for j in i if j.isnumeric()])
        
        # Get int of position - 11 if DNF.
        res = int(res if res else 11)

        # If points scoring position, update total score.
        # Ensuring +1 for fastest lap, if applicable.
        if res<=10:
            total += points[res-1] + ("F" in i)
    
    # Add drivers points and name to drivers array.
    drivers += [[total , name]]

# Sort based on points only (Keeps order of equal points)
drivers.sort(key = lambda driver : driver[0])

# Output name of driver in order.
for _,name in drivers[::-1]:
    print(name)


"""
# Solution without comments.
points = [25,18,15,12,10,8,6,4,2,1]
drivers = []
n = int(input())
for _ in range(n):
    name,results = input().split(":")
    total = 0
    for i in results.split(" "):
        res = "".join([j for j in i if j.isnumeric()])
        res = int(res if res else 11)
        if res<=10:
            total += points[res-1] + ("F" in i)
    drivers += [[total , name]]
drivers.sort(key = lambda driver : driver[0])
for _,name in drivers[::-1]:
    print(name)
"""
