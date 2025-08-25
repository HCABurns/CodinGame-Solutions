from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.tree = Node(None)

    def add(self, val):
        if self.tree.val == None:
            self.tree.val = val
            return
        tmp = self.tree
        while tmp != None:
            if val > tmp.val:
                if tmp.right:
                    tmp=tmp.right
                else:
                    tmp.right = Node(val)
                    return
            else:
                if tmp.left:
                    tmp = tmp.left
                else:
                    tmp.left = Node(val)
                    return
        #tmp = Node(val)

# Form Tree.
tree = Tree()
n = int(input())
for i in input().split():
    vi = int(i)
    tree.add(vi)

# Perform Pre-In-Post-Level order on the tree.
outputs = [[] for i in range(4)]
def search1(tree, i):
    if tree:
        outputs[i].append(tree.val)
        search1(tree.left, i)
        search1(tree.right, i)
        
def search2(tree, i):
    if tree:
        search2(tree.left, i)
        outputs[i].append(tree.val)
        search2(tree.right, i)

def search3(tree, i):
    if tree:
        search3(tree.left, i)
        search3(tree.right, i)
        outputs[i].append(tree.val)

def search4(tree, i):
    to_visit = deque([tree])
    while to_visit:
        node = to_visit.popleft()
        outputs[i].append(node.val)
        if node.left:
            to_visit.append(node.left)
        if node.right:
            to_visit.append(node.right)
search1(tree.tree, 0)
search2(tree.tree, 1)
search3(tree.tree, 2)
search4(tree.tree, 3)

# Print the results.
for i in outputs:
    print(" ".join([str(j) for j in i]))
