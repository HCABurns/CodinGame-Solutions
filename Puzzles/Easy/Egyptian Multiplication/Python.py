# Get numbers and total.
a, b = [int(i) for i in input().split()]
total = a*b

# Swap if required.
if a > b:
    a , b = b , a

# Print and perfrom operations in required manner.
print(b,"*",a)
values = []
while a > 0:
    if a % 2 == 1:
        a -= 1
        values.append(str(b))
    else:
        a //= 2
        b *= 2
    if len(values) == 0:
        print("=",b,"*",a)
    else:
        print("=",b,"*",a, "+"," + ".join(values))
print("=",total)
