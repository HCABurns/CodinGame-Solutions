# Hashmap for storing cars and array for storing speeding cars.
cars = {}
speeding = []

# Get speed limit and number of readings.
l = int(input())
n = int(input())

# Find speed between readings and determine if speeding or not.
for i in range(n):
    reg, dist, time = input().split(" ")
    dist, time = map(int, [dist,time])
    
    if reg in cars:
        dist2, time2 = cars[reg]

        speed = (dist - dist2) / ((time-time2) / 3600.0)
        if speed > l:
            speeding.append(reg + " " + str(dist))
    cars[reg] = [dist, time]

# Print speeding cars otherwise OK
if speeding:
    print(*speeding ,sep = "\n")
else:
    print("OK")
