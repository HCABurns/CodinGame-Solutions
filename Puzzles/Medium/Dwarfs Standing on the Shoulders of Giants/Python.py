class Node:
    """
    Helper function to hold id and children of node.

    Methods:
    __init__(id) - Initialise a node with given id.
    add_child(id) - Adds id to children array.
    get_id - Return id of node.
    get_children - Returns array of children.
    """
    def __init__(self,id):
        self.id = id
        self.children = []

    def add_child(self,id):
        self.children.append(id)

    def get_id(self):
        return self.id

    def get_children(self):
        return self.children

# Form graph using node class.
nodes = {}
n = int(input()) 
for i in range(n):
    x, y = [int(j) for j in input().split()]

    if x not in nodes:
        nodes[x] = Node(x)
    if y not in nodes:
        nodes[y] = Node(y)

    nodes[x].add_child(y)

# DFS to find longest path - Using cache to speed up searching (0<N<10000 so may be required)
cache = {}
def search(node):
    # Check in cache to speed up searching.
    if node in cache:
        return cache[node]

    # Get children.
    children = nodes[node].get_children()

    # If 'leaf' node - End of path so return 1.
    if len(children) == 0:
        return 1
    
    # Initialise length.
    length = 0

    # Recursive DFS to find max length of path that reaches a 'leaf'.
    for child in children:
        res = search(child)
        if res:
            length = max(length, res+1)
    
    # Cache and return.
    cache[node] = length
    return length

# Output the number of people involved in the longest succession of influences
vals = []
for i in nodes:
    vals.append(search(i))
print(max(vals))
