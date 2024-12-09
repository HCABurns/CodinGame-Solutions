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
    drivers += [(total , name)]
drivers.sort(key = lambda driver : driver[0] , reverse = True)
for _,name in drivers:
    print(name)
"""

#Solution with comments.
# Arrays for position and points.
points = [25,18,15,12,10,8,6,4,2,1]
drivers = []

results_test = []
length = -1

n = int(input())
for _ in range(n):
    # Split name and results.
    name,results = input().split(":")
    
    # TESTING ENSURE all contain same number of results
    if length == -1:
        length = len(results.split(" "))
    else:
        assert length == len(results.split(" ")), "Missing results: {results}"
    
    # Drivers points total.
    total = 0
    idx = 0
    for i in results.split(" "):
        # Get position in race.
        res = "".join([j for j in i if j.isnumeric()])
        
        # Get int of position - 99 if DNF.
        res = int(res if res else 99)

        if len(results_test) <= idx:
            results_test.append([])
            results_test[idx].append(i)
        else:
            results_test[idx].append(i)
        idx+=1

        # If points scoring position, update total score.
        # Ensuring +1 for fastest lap, if applicable.
        if res<=10:
            total += points[res-1] + ("F" in i)
    
    # Add drivers points and name to drivers array.
    drivers.append((total , name))

# Sort.
drivers.sort(key = lambda driver : driver[0] , reverse = True)

# Output name of driver in order.
for score,name in drivers:
    print(name)# , score)

# TESTING
for idx,i in enumerate(results_test):
    test_dnf_removed = [int("".join([c for c in j if c.isnumeric()])) for j in i if "DNF" not in j and j!=99]
    s = sum(str(j).count("F") if "DNF" not in j else str(j).count("F")-1 for j in i )
    assert s == 1, f"No Fastest lap at race :{idx+1} sum={s}"
    assert len(set(test_dnf_removed)) == len(test_dnf_removed), f"DUPLICATE: {sorted(test_dnf_removed)} in race: {idx+1}"
    assert sorted(test_dnf_removed) == list(range(1,len(test_dnf_removed)+1)), f"Race {idx+1}: Order wrong: {sorted(test_dnf_removed)} , Expected: {list(range(1,len(test_dnf_removed)+1))}" 
