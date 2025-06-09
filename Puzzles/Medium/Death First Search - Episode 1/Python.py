from collections import deque

# Generate Graph - id: children
graph = {}
# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
for i in range(l):
    # N1 and N2 defines a link between these nodes.
    n1, n2 = [int(j) for j in input().split()]
    if n1 not in graph:
        graph[n1] = []
    if n2 not in graph:
        graph[n2] = []
    graph[n1]+=[n2]
    graph[n2]+=[n1]

# Add the index of a gateway node to the set.
gateways = set()
for i in range(e):
    gateways.add(int(input()))
import random
# Continue until the virus can't access a gateway.
while True:
    # The index of the node on which the Bobnet agent is positioned this turn
    si = int(input())  

    # Define queue to perform a BFS.
    to_visit = deque([si])
    
    # Required variable for the BFS.
    found = False
    idx = si
    node = si
    
    # Perform a BFS until the closest connection to a gateway is found and print to break.
    while to_visit:
        idx = to_visit.popleft()
        nodes = graph[idx]
        for node in nodes:
            if node in gateways:
                graph[idx].remove(node)
                graph[node].remove(idx)
                found = True
                break
            #to_visit.append(node)
          if found:break
    
    # Print the link to break.
    print(idx, node)
