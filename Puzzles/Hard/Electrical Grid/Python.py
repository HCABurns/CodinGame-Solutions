# Form connections.
connections = []
n, m = [int(i) for i in input().split()]
for i in range(m):
    house_1, house_2, cost = [int(j) for j in input().split()]
    connections.append([cost,house_1-1,house_2-1])
connections.sort()

# Kruskals MST algorithm.
weights = []
used = []
parent = list(range(n))
rank = [0] * (n)
def find_rep(house):
    if parent[house] != house:
        parent[house] = find_rep(parent[house])
    return parent[house]

def union(h1,h2):
    u_rep = find_rep(h1)
    v_rep = find_rep(h2)
    if u_rep != v_rep:
        if rank[u_rep] > rank[v_rep]:
            parent[v_rep] = u_rep
        elif rank[u_rep] < rank[v_rep]:
            parent[u_rep] = v_rep
        else:
            parent[v_rep] = u_rep
            rank[u_rep] += 1

def kruskals():
    for con in connections:
        cost, h1, h2 = con
        if find_rep(h1) != find_rep(h2):
            union(h1,h2)
            weights.append(cost)
            used.append([h1+1,h2+1,cost])
kruskals()

# Print result.
print(len(weights) , sum(weights))
for con in sorted(used):
    print(" ".join(map(str,con)))
