singles = {val:f"{val}" for val in [i for i in range(1,21)]+[25]}
doubles = {val:f"D{val//2}" for val in [i*2 for i in range(1,21)]+[50]}
trebles = {val:f"T{val//3}" for val in [i*3 for i in range(1,21)]}

combinations = []
def search(score, darts, left):
    if score < 0 or left == -1:
        return 0
    
    if score == 0 and len(darts)>=1 and "D" in str(darts[-1]):
        if darts not in combinations:
            combinations.append(darts)
        return 1

    if left > 1:
        for arr in [singles, doubles, trebles]:
            for dart, dart_str in arr.items():
                search(score - dart, darts+[dart_str], left - 1)         
    else:
        for dart, dart_str in doubles.items():
            search(score - dart, darts+[dart_str], left - 1)
    return

score, darts = int(input()), int(input())
search(score, [], darts)
print(len(combinations))
