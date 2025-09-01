# Get peoples id and the names.
people = {}
c = int(input())
for i in range(c):
    people[input()] = i+1

# Store the votes.
votes = []
v = int(input())
for i in range(v):
    vote = list(map(int,input().split()))
    votes += [vote]

# Complete each round storing the name of those eliminated.
eliminated = []
for i in range(c): # Round
    round_votes = {people[name]:[0,name] for i,name in enumerate(people.keys(),1) if name not in eliminated}
    for j in range(v): # Votes #
        for vote in votes:
            for val in vote:
                if val in round_votes:
                    round_votes[val][0] += 1
                    break
    
    round_votes = sorted(round_votes.values(),key = lambda x: x[0])
    eliminated += [round_votes[0][1]]

# Print the names in order.
eliminated[-1] = "winner:"+eliminated[-1]
for name in eliminated:
    print(name)
