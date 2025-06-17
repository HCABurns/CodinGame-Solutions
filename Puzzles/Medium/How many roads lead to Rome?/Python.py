from collections import defaultdict, deque

# Form Graph.
graph = defaultdict(list)
n = int(input())
for i in range(n):
    f, to = map(int,input().split())
    graph[f].append(to)
    graph[to].append(f)

# Perform BFS to find valid paths from 1 to 100.
queue = deque([[1,[1]]])
paths = set()
while queue:
    node, path = queue.popleft()
    if node == 100:
        paths.add(tuple(path))

    for children in graph[node]:
        if children not in path:
            queue.append([children, path+[children]])

# Print the number of paths from 1 to 100. (Paris to Rome)
print(len(paths))
