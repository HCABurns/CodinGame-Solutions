# Hashmap for converting
units = ["um","mm","cm","dm","m","km"]
meter_conversion=[6,3,2,1,0,-3]# To meters

# Get left and right
left, right = input().split(" + ")

# Get values.
left_value = float("".join([str(i) for i in left if i.isnumeric() or i == "."]))
right_value = float("".join([str(i) for i in right if i.isnumeric()or i == "."]))

# Get units.
left_units = "".join([i for i in left if i.isalpha()])
right_units = "".join([i for i in right if i.isalpha()])

# Get index of units.
lidx = units.index(left_units)
ridx = units.index(right_units)

# Convert the larger to the smaller units.
if lidx == ridx:
    units = left_units
elif lidx > ridx:
    #Convert both to meter
    left_value *= 10**-(meter_conversion[lidx])
    units = right_units
    left_value *= 10**(meter_conversion[ridx])

elif lidx < ridx:
    right_value *= 10**-(meter_conversion[ridx])
    units = right_units
    right_value *= 10**(meter_conversion[ridx])

# Print the calculation in the smaller units.
sum_val = left_value + right_value
if sum_val == sum_val // 1:
    sum_val = int(sum_val)
else:
    if units == "um":
        sum_val = round(sum_val,2)
print(f"{sum_val}{units}") 
