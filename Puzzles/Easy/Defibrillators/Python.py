import math

# Convert longitude and latitude to float values.
lon = float(input().replace(",","."))
lat = float(input().replace(",","."))

# Create array for storing values.
out = []

# Go through each inputs, storing the distance and the name.
for i in range(int(input())):
    defib = input()
    s = defib.split(";")
    x = (float(s[-2].replace(",","."))-lon) * math.cos((float(s[-2].replace(",","."))+lon)/2)
    y = (float(s[-1].replace(",","."))-lat)
    d = (x**2 + y**2)**0.5 * 6371
    out.append((d,s[1])) 

# Find the closest value and output the name.
out.sort(key = lambda x : x[0])
print(out[0][1])
