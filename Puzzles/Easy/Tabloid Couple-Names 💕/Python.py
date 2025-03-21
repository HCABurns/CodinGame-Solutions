# Get number of couples.
n = int(input())

# Find tabloid Couple-Names.
for _ in range(n):
    # Get both names.
    inputs = input().split(" ")
    name1, name2 = inputs[0], inputs[2]
    
    # Convert to lower for comparisions.
    n1 = name1.lower()
    n2 = name2.lower()

    # Find overlapping substrings.
    substrings = []
    overlaps = []
    for idx in range(0,len(n1)):
        [substrings.append(n1[idx:i])for i in range(1,len(n1)+1) if n1[idx:i] != ""]
    for idx in range(0,len(n2)):
        [overlaps.append(n2[idx:i]) for i in range(1,len(n2)+1) if n2[idx:i] != ""]
    
    # Find all possible tabloid names.
    words = []
    for overlap in overlaps:
        for n1,n2 in [[n1,n2] , [n2,n1]]:
            for w1_idx in range(0,len(n1)-len(overlap)+1):
                if n1[w1_idx:w1_idx+len(overlap)] == overlap:
                    for w2_idx in range(0,len(n2)-len(overlap)+1):
                        if n2[w2_idx:w2_idx+len(overlap)] == overlap:
                            words.append((n1[:w1_idx+len(overlap)] + n2[w2_idx+len(overlap):] , len(overlap)))


    # Find only valid words, then select all those names with max number of overlapping characters.
    words = [(i,v) for i,v in words if i not in n1 and i not in n2 and len(i) >= min(len(n1),len(n2))]
    max_v = max([v for _,v in words]) if words else []
    words = [i.capitalize() for i,v in words if v == max_v]
    
    # Print names or None if no valid tabloid names.
    print(f'{name1} plus {name2} = {" ".join(sorted(list(set(words)))) if words else "NONE"}')
