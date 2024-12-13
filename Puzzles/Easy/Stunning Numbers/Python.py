# Get number to check.
n = input()
value_n = int(n)

# Hashmap for ,,,
reverse = {"6":"9","9":"6"}
invalid = {"3","4","7"}
translation = str.maketrans("69347", "96558")

# Check if n if a stunning number.
swapped = "".join([reverse.get(i,i) for i in n][::-1])
if n.translate(translation)[::-1] != n:
    print("false")
else:
    print("true")

# Get next number
value = value_n+1
value = str(value)

# Find next stunning number.
while True:
    if any(1 if i in invalid else 0 for i in value):
        # Set new value, increment first invalid digit and set any following digits to 0
        new_value = 0
        shifted = False
        for val in value:
            if shifted:
                new_value = new_value * 10
            elif val not in invalid: 
                new_value = new_value * 10 + int(val)
            else:
                new_value = new_value * 10 + int(val) + 1
                shifted=True
        
        # Get new value with mirroring.
        new_value = str(new_value)
        value = new_value[:(len(new_value)+1) // 2]
        if (len(new_value)) % 2 == 1:
            value = value + [value.translate(translation)[:-1][::-1],value.translate(translation)][len(value)==1]
        else:
            value = value + value.translate(translation)[::-1] 

    #Check if stunning number.
    if value == value.translate(translation)[::-1] and int(value) > value_n:
        break
    
    # Increment value.
    int_value = str(int(value))
    value_before = str(int(value[:(len(value)+1) // 2]))
    value = str(int(value[:(len(value)+1) // 2])+1)

    # Reverse first half and append to back (Special case for 9-10, 99-100 etc.)
    if len(value_before) != len(value):
        if len(value_before) % 2 == 0:
            value = value + [value.translate(translation)[:-1][::-1],value.translate(translation)][len(value)==1]
        else:
            value = value + [value.translate(translation)[:-2][::-1],value.translate(translation)][len(value)==1]
    elif (len(int_value)) % 2 == 1:
        value = value + [value.translate(translation)[:-1][::-1],value.translate(translation)][len(value)==1]
    else:
        value = value + value.translate(translation)[::-1]

# Print next stunning number.
print(value)
