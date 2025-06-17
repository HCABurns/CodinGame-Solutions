from collections import defaultdict, deque

graph = defaultdict(list)

# Read graph
for _ in range(int(input())):
    thread = input().split()
    for name1, name2 in zip(thread[:-1],thread[1:]):
        graph[name1].append(name2)
        graph[name2].append(name1)

# BFS to find connected components
seen = set()
group_count = 0

for name in graph:
    if name in seen:
        continue
    queue = deque([name])
    while queue:
        current = queue.popleft()
        if current in seen:
            continue
        seen.add(current)
        queue.extend(graph[current])
    group_count += 1

print(group_count)
