# Define the pins and their values.
nums = [f"P{i}" for i in range(1, 13)] + [i for i in range(2, 13)]
values = {f"P{i}": i for i in range(1, 13)} | {i: i for i in range(2, 13)}
values_reverse = {i: f"P{i}" for i in range(1, 13)}

# Get the starting number.
n = int(input())

# Define results , goal value and the cache.
result = set()
cache = {}
goal_value = 50

# Complete DFS to find the combinations to reach 50.
def search(total, index, turns, path):
    # Goal state.
    if total ==goal_value:
        result.add(tuple(path))
        result.add(tuple(path[::-1]))
        return 1

    # Check cache / memo for already checked paths.
    if (total, index, turns, path) in cache:
        return 0
    cache[(total, index, turns, path)] = 0

    # Perform final pin calculations (Saves extra recursive calls)
    if turns == 3:
        needed =goal_value - total
        if 1 <= needed <= 12:
            options = []
            if needed in values:
                options.append(needed)
            if f'P{needed}' in values:
                options.append(f'P{needed}')
            for final in options:
                p = tuple(path + (final,))
                result.add(p)
                result.add(p[::-1])
            return 1
        return 0

    # Error checking.
    if turns >= 4 or index >= len(nums):
        return 0

    # Check all possible pins for path.
    for idx in range(0, len(nums)):
        j = nums[idx]
        v = values[j]
        if total + v >goal_value:
            continue
        search(total + v, idx, turns + 1, path + (j,))
        search(total, idx + 1, turns, path)
    return 0

# Perfrom DFS to find ways to reach 50 from n.
search(n, 0, 0, ())

# Print number of ways to reach 50 from n.
print(len(result))
