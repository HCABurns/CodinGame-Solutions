from collections import defaultdict

# Dictionary and set for storing information about the rooms.
room_money = defaultdict(int)
graph = defaultdict(list)
ends = set()

# From graph.
n = int(input())
for i in range(n):
    room, money, to, to2 = input().split(" ")
    room = int(room)
    room_money[room] = int(money)

    if to == "E":
        ends.add(room)
    else:
        to = int(to)
        graph[room].append(to)
        graph[room] = sorted(graph[room], key = lambda x : room_money[x])
    if to2 == "E":
        ends.add(room)
    else:
        to2 = int(to2)
        graph[room].append(to2)
        graph[room] = sorted(graph[room], key = lambda x : room_money[x])

# Store the best known cash for each room
best_cash = [-1]*n
best_cash[0] = room_money[0]

# DFS
stack = [0]
while stack:
    # Get room.
    room = stack.pop()

    # Check next rooms.
    for nxt in graph[room]:
        new_cash = best_cash[room] + room_money[nxt]
        # If better way to reach that room, store and search again.
        if new_cash > best_cash[nxt]:
            best_cash[nxt] = new_cash
            stack.append(nxt)

result = max(best_cash[r] for r in ends)
print(result)
