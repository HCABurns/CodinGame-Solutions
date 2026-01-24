from collections import deque
from collections import defaultdict

# Form Graph.
graph = defaultdict(list)
n, m = [int(i) for i in input().split()]
s, e = [int(i) for i in input().split()]
for i in range(m):
    a, b, t = [int(j) for j in input().split()]
    graph[a].append([b,[t]])
    graph[b].append([a,[t]])

# Form to_visit queue.
to_visit = deque()
for node in graph[s]:
    to_visit.append(node+[1,{node[0]}])

# Perform BFS to find the minimum path length.
def bfs():
    while to_visit:
        # Get next node.
        (node, fuses, path_length, visited) = to_visit.popleft()
        
        # Ensure no fuses have blown.
        if any(1 for fuse in fuses if fuse == 0):
            continue 

        # If goal node reached, return length to reach it.
        if node == e:
            return path_length
        
        # Perform BFS if the node hasn't been visited.
        for next_node,fuse in graph[node]:
            if next_node not in visited:
                to_visit.append([next_node, [val-1 for val in fuses]+fuse, path_length+1, visited | {next_node}])
    return "IMPOSSIBLE"
# Print the minimum path from start to end otherwise "IMPOSSIBLE" if it can't be reached.
print(bfs())
