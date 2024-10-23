# game loop
while True:
    # Fill array with the heights of the mountains.
    arr = []
    for i in range(8):
        mountain_h = int(input())
        arr.append(mountain_h)
    
    #Output the index of the max value in the array.
    print(arr.index(max(arr)))
