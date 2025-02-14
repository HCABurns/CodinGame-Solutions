#Array for storing units and conversion numbers.
units = ["miles","furlongs","chains","yards","feet","inches"]
time_units = ["fortnight","week","day","hour","minute","second"]
dist = [1,8,10,22,3,12]
time = [1,2,7,24,60,60]

# Get input and parse to get relevant info.
a_speed = input()

l , r = a_speed.split(" CONVERT TO ")
value, units1, _, time1 = l.split()
units2, _, time2 = r.split()
value = float(value)

# Get the index of the time units.
idx1 = time_units.index(time1)
idx2 = time_units.index(time2)

# Convert value to requried units. 
while idx2 > idx1:
    value /= time[idx1+1]
    idx1+=1

while idx2 < idx1:
    value *= time[idx2+1]
    idx2+=1

# Get the index of the distance units.
idx1 = units.index(units1)
idx2 = units.index(units2)

# Convert value to requried units.
while idx2 > idx1:
    value *= dist[idx1+1]
    idx1+=1

while idx2 < idx1:
    value /= dist[idx2+1]
    idx2+=1

# Print the converted value
print(f"{round(value,1)} {units2} per {time2}")
