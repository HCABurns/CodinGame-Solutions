# Required import.
from collections import defaultdict

# Graph to store if a switch is set to ON OR OFF
switches_positions = defaultdict(int)
wiring_positions = defaultdict(list) #0 Indicates series and 1 indicates parallel

# Form circuit.
c = int(input())
for i in range(c):
    name, *wiring = [*input().split()]
    for switch in wiring:
        if switch == "-":
            wiring_positions[name].append([0])
        elif switch == "=":
            wiring_positions[name].append([1])
        else:
            wiring_positions[name][-1].append(switch)

# Press switches.
a = int(input())
for i in range(a):
    switch = input()
    switches_positions[switch] ^= 1

# Follow circuit finding if any are not switched on - break and output.
for name, wires in wiring_positions.items():
    valid = True
    for wire_set in wires:
        if wire_set[0] == 0:
            valid = all(switches_positions[wire] for wire in wire_set[1:])
        else:
            valid = any(switches_positions[wire] for wire in wire_set[1:])
        if not valid:
            break
    print(name,"is",["OFF","ON"][valid])

