from collections import defaultdict
from collections import deque

# Set graph.
graph = defaultdict(list)

# Get start and end and form graph.
start = input()
end = input()
n = int(input())
for i in range(n):
    station_1, station_2 = input().split()
    graph[station_1].append(station_2)
    graph[station_2].append(station_1)

# Complete a BFS until the path is found.
queue = deque([[start,[start]]])
while queue:
    current_station, path = queue.popleft()

    # Path found, print the path.
    if current_station == end:
        print(" > ".join(path))
        break

    for con in graph[current_station]:
        if con not in path:
            queue.append([con, path+[con]])

