from collections import deque

h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

def search(start_i, start_j):
    queue = deque([(start_i, start_j)])
    grid[start_i][start_j] = "."
    positions = [(0, 0)] 
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        i, j = queue.popleft()
        for dy, dx in directions:
            ny, nx = i + dy, j + dx
            if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == "*":
                grid[ny][nx] = "."
                queue.append((ny, nx))
                positions.append((ny - start_i, nx - start_j))
    return positions

snowflake_patterns = set()
snowflakes = 0
unique_snowflakes = 0

for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if char == "*":
            positions = search(i, j)
            snowflakes += 1

            variations = []
            for base in [positions, [(y, -x) for (y, x) in positions]]:
                current = base
                for _ in range(4):
                    min_x = min(x for x, _ in current)
                    min_y = min(y for _, y in current)
                    norm = sorted((x - min_x, y - min_y) for x, y in current)
                    variations.append(tuple(norm))
                    current = [(y, -x) for (x, y) in current]

            if any(variation not in snowflake_patterns for variation in variations):
                for variation in variations:
                    snowflake_patterns.add(variation)
                unique_snowflakes += 1

print(snowflakes)
print(unique_snowflakes)
