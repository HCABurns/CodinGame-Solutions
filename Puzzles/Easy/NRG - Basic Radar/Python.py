# Create hashmap and array to store values.
hashmap = {}
arr = []
n = int(input())

# For each plane, store it's timestamp and plate. Once it is found again, calculate it's speed and if it's over 130km/h, then store.
for i in range(n):
    # Split inputs into reqiured information.
    inputs = input().split()
    plate = inputs[0]
    timestamp = int(inputs[2])

    # If plane has not been found yet then add to hashmap with timestamp.
    if plate not in hashmap:
        hashmap[plate] = timestamp
    # If plane passes second checkpoint, calculate speed and store if over 130km/h.
    else:
        time = timestamp - hashmap[plate]
        s = 13 // (time/1000/60/60)
        if s > 130:
            arr.append((plate,(int)(s)))

# Sort array on speed.
arr.sort(key=lambda tup: tup[0])

# Output plane if speed is over 130km/h.
for each in arr:
    print("{} {}".format(each[0],each[1]))
