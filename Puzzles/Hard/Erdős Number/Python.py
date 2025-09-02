from collections import defaultdict
from collections import deque

titles = defaultdict(list)
connections = defaultdict(list)

# Get titles of publications.
t = []
scientist = input()
n = int(input())
for i in range(n):
    title = input()
    t.append(title)

# Link papers to scientists and scientists together.
for i in range(n):
    title = t[i]
    authors = input().split()

    for author in authors:
        titles[author].append(title)

    for author in authors:
        for author2 in authors:
            if author==author2:continue
            else:
                connections[author].append(author2)

# Find minimum links top Erdos.
min_links = -1
queue = deque([[scientist, 1, [scientist]]])
seen = set(scientist)
found = False
while queue:

    author, links, people = queue.popleft()
    if author == "Erdős":
        found = True
        min_links = links-1
        break

    for collab in connections[author]:
        if collab not in seen:
            seen.add(collab)
            queue.append([collab, links+1, people + [collab]])

# Print min_links or infinite. If min_links is possible and > 0, print the papers
# linking scientist to Erdos.
if found:
    print(min_links)
    if min_links > 0:
        seen = set()
        for a,b in zip(people,people[1:]):
            for title in titles[a]:
                if title in titles[b]:
                    if title not in seen:
                        seen.add(title)
                        print(title)
                        break
else:
    print("infinite")
