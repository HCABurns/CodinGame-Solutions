# Import for angle calculations.
from math import atan
from math import pi

# Class for storing an island.
class Island():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def distance_to(self, island): return ((self.x - island.x)**2 + (self.y - island.y)**2 + (self.z - island.z)**2) ** 0.5
    def get_coords(self): return [self.x , self.y, self.z]
    def angle_and_distance(self, neighbour):
        #Toa - Opposite is ∆Z and adjacent is ∆xy
        x2, y2, z2 = neighbour.get_coords()
        distance = self.distance_to(neighbour)
        horizontal_distance = ((x2 - self.x)**2 + (y2 - self.y)**2) ** 0.5
        if horizontal_distance == 0:
            angle = 90
        else:
            angle = round(atan(abs(z2 - self.z)/horizontal_distance)*(180/pi),2)
        return distance, angle

# Array for storing islands.
islands = [Island(1,1,1)]

# Populate islands array with n islands.
n = int(input())
for i in range(n):
    x, y, z = map(float, input().split())
    assert -3000 <= x <= 3000, f"{x} X not in range"
    assert -3000 <= y <= 3000, f"{y} Y not in range"
    assert 1 <= z <= 5000, f"{z} Z not in range"
    islands.append(Island(x,y,z))

# Form graph.
DISTANCE_THRESHOLD = 1000
ANGLE_THRESHOLD = 45
edges = []
for i, island in enumerate(islands):
    for j in range(i+1,len(islands)):
        distance, angle = island.angle_and_distance(islands[j])
        if angle <= ANGLE_THRESHOLD and distance <= DISTANCE_THRESHOLD:
            edges.append([distance, i, j])

# Kruskal's Algorithm for MST.
edges.sort(key=lambda x: x[0])
parent = list(range(len(islands)))
rank = [0] * len(islands)  
total_distance = 0
leftover_wood = []

# Function to find representative for a tree.
def find_rep(node):
    if parent[node] != node:
        parent[node] = find_rep(parent[node])
    return parent[node]

# Function to combine two trees into one.
def union(u, v):
    u_rep = find_rep(u)
    v_rep = find_rep(v)
    if u_rep != v_rep:
        if rank[u_rep] > rank[v_rep]:
            parent[v_rep] = u_rep
        elif rank[u_rep] < rank[v_rep]:
            parent[u_rep] = v_rep
        else:
            parent[v_rep] = u_rep
            rank[u_rep] += 1

for weight, u, v in edges:
    if find_rep(u) != find_rep(v):
        union(u, v)
        total_distance += weight
        # Find the first reusable tree or cut down a new one.
        reused_tree_idx = next((i for i, tree in enumerate(leftover_wood) if tree >= weight), None)
        if reused_tree_idx is not None:
            leftover_wood[reused_tree_idx] -= weight
        else:
            leftover_wood.append(DISTANCE_THRESHOLD - weight)

# Output the required variables.
print("%.02f"%total_distance)
print("%.02f"%sum(leftover_wood))
print(len(leftover_wood))

# TESTING: Ensure that all islands are in the same tree.
final_representatives = set(find_rep(i) for i in range(len(islands)))
assert len(final_representatives) == 1, f"Disconnected representatives: {final_representatives}"
