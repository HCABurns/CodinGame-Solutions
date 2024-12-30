# Get voters and number of votes allowed.
n = int(input())
m = int(input())
voters = {}
for i in range(n):
    inputs = input().split()
    person_name = inputs[0]
    nb_vote = int(inputs[1])
    voters[person_name] = nb_vote

# Keep store of votes, names, vote results and any invalid names.
votes = [0,0]
names = []
res = []
invalid = []
for i in range(m):
    voter_name, vote_value = input().split()
    names.append(voter_name)
    res.append(vote_value)
    if names.count(voter_name) > voters.get(voter_name,1e9):
        invalid.append(voter_name)

# Add results only if valid voter.
for name, vote_value in zip(names,res):
    if name not in invalid and voters.get(name,-1) > 0 and vote_value in ["Yes" , "No"]:
        voters[name] -= 1
        votes[vote_value == "No"] += 1

# Print Yes and No totals.
print(*votes)
