# Get number of inputs.
n = int(input())

# Create registers and set for storing operations.
graph = {i:-99999 for i in range(n)}
operations = set()
ops = {"MULT":"*","ADD":"+","SUB":"-"}

# Store the operations in an array.
for i in range(n):
    operations.add((i, *input().split()))

# Loop through the operations completing operations when they're possible.
while operations:
    to_remove = []
    for operation in operations:
        i, op , v1, v2 = operation

        # Convert any reference to registers to values.
        if "$" in v1:
            v1 = graph[int(v1[1:])]
        if "$" in v2:
            v2 = graph[int(v2[1:])]

        # Check that they have valid values, if so perform operation.
        if v1 != -99999 and v2 != -99999:
            if op == "VALUE":
                graph[int(i)] = int(v1)
            else:
                graph[i] = eval(f"{v1}{ops[op]}{v2}")
            to_remove.append(operation)
    
    # Remove any completed operations.
    for operation in to_remove:
        operations.remove(operation)

# Print the result.
for i in range(n):
    print(graph[i])
