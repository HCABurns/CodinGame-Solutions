singles = {val:f"{val}" for val in [i for i in range(1,21)]+[25]}
doubles = {val:f"D{val//2}" for val in [i*2 for i in range(1,21)]+[50]}
trebles = {val:f"T{val//3}" for val in [i*3 for i in range(1,21)]}

combinations = set()
def search(score, darts, left):
    if score < 0 or left == -1:
        return
    
    if score == 0 and darts and "D" in str(darts[-1]):
        combinations.add(tuple(darts))
        return

    for arr in [singles, doubles, trebles] if left > 1 else [doubles]:
        for dart, dart_str in arr.items():
            search(score - dart, darts+[dart_str], left - 1)         
    return

score, darts = int(input()), int(input())
search(score, [], darts)
print(len(combinations))
