from collections import defaultdict

# Form Linked-List.
class Node:
    def __init__(self, id, next):
        self.id = id
        self.next = next
head = Node(None, None)
dummy_head = head

# Define friend groups.
groups = defaultdict(set)
g, e = [int(i) for i in input().split()]
for i in range(g):
    group = input().split(" ")
    for p1 in group:
        for p2 in group:
            if p1==p2:continue
            groups[int(p1)].add(int(p2))
            groups[int(p2)].add(int(p1))

# Simulate the queueing of students next to their friends and dequeueing.
for i in input().split():
    event = int(i)
    head = dummy_head
    if event == -1:
        print(dummy_head.id)
        dummy_head = dummy_head.next if dummy_head.next else Node(None,None)
    else:
        head = dummy_head
        prev = None
        while head.next:
            if head.id in groups[event]:
                while head and head.id in groups[event]:
                    prev = head
                    head = head.next
                break
            head = head.next
        
        if not dummy_head.id:
            head.id = event
        elif prev:
            prev.next = Node(event, prev.next)
        else:
            head.next = Node(event, None)
