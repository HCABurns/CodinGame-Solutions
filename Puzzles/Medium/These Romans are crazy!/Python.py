# Get roman.
rom_1 = input()+" "
rom_2 = input()+" "

values = "1 4 5 9 10 40 50 90 100 400 500 900 1000".split(" ")
symbols = "I IV V IX X XL L XC C CD D CM M".split(" ")
hashmap = {s:int(v) for s,v in zip(symbols,values)} | {v:s for s,v in zip(symbols,values)}

# Convert roman to int.
def roman_to_int(value):
    total = 0
    for i in range(len(value)-1):
        if hashmap[value[i]] < hashmap.get(value[i+1],-1):
            total -= hashmap[value[i]] 
        else:
            total += hashmap[value[i]] 
    return total

# Get total of addition.
total = roman_to_int(rom_1) + roman_to_int(rom_2)

# Convert the total back to roman.
roman = ""
while total > 0:
    for value in values[::-1]:
        while int(value) <= total:
            total -= int(value)
            roman += hashmap[value]

# Print the roman of the addition.
print(roman)
