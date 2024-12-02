class Node():
    """
    Class to hold information about a node.
    """
    def __init__(self, idx, parent,direction):
        self.idx = idx
        self.parent = parent
        self.direction = direction

# Hashmap for storing node.s
nodes = {}

# Get input.
n = int(input())
v = int(input())
m = int(input())

# Create tree.
for i in range(m):
    p, l, r = [int(j) for j in input().split()]

    # Add nodes if not seen yet.
    if p not in nodes:
        nodes[p] = Node(p,None,None)
    
    if l not in nodes:
        nodes[l] = Node(l, nodes[p],"Left")

    if r not in nodes:
        nodes[r] = Node(r,nodes[p],"Right")

# Get route from node to root.
out = []
while nodes[v].parent != None:
    out += [nodes[v].direction]
    v = nodes[v].parent.idx

# Print route from root to node or "Root" if root node.
if out:
    print(" ".join(out[::-1]))
else:
    print("Root")
