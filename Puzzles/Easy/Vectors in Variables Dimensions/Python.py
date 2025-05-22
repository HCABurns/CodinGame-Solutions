# Array for storing coordinates.
coordinates = []

# Read in the coordinates and store.
d = int(input())
n = int(input())
coordinates = []
for i in range(n):
    name, pos = input().split("(")
    pos = pos[:-1].split(",")
    coordinates.append([name, [int(value) for value in pos]])

# Compare all the vectors storing distance with the information about the vector.
vectors = []
for i,(name1, pos1) in enumerate(coordinates):
    for j in range(i+1,len(coordinates)):
        name2, pos2 = coordinates[j]
        dist = 0
        dists = []
        for v1, v2 in zip(pos1, pos2):
            dist += (v1-v2)**2
            dists.append(str(v2-v1))
        vectors.append([dist,name1+name2+"("+",".join(dists)+")"])

# Sort the vectors and print the shortest and largest.
vectors.sort()
print(vectors[0][1])
print(vectors[-1][1])
