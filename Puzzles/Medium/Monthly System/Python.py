# Hashmap for storing values.
hashmap = {
"Jan":0,
"Feb":1,
"Mar":2,
"Apr":3,
"May":4,
"Jun":5,
"Jul":6,
"Aug":7,
"Sep":8,
"Oct":9,
"Nov":10,
"Dec":11,
}
for key,val in list(hashmap.items()):
    hashmap[val] = key


# Get values and convert to base-12 numbers.
values = []
n = int(input())
for i in range(n):
    m = input()
    for idx,j in enumerate(range(len(m),0,-3)):
        month = m[j-3:j]
        if len(values) <= idx:
            values += [0]
        values[idx] += hashmap[month]

# Add together.
out = []
carry = 0
for sum_val in values:
    out += [sum_val % 12 + carry]
    carry = sum_val // 12
if carry:
    out += [carry]

# Convert back to month format.
leading_zero = True
for i,val in enumerate(out[::-1]):
    if val == 0 and leading_zero:
        out[i] = ""
        continue
    leading_zero = False

    out[i] = hashmap[val]

# Print.
print("".join(out))
