# Get input number.
begin = n = int(input())

# Store sign and convert to positive.
sign = 1 if n > 0 else -1
n = abs(n)

# Convert to Base 3 - T represents -1: remainder 2 == remainder -1 with n+1
out = ""
while n > 0 or n < 0:
    rem = n%3
    if rem == 2:
        out+="T"
        n+=1
    else:
        out+=str(rem)
    n//=3

# If negative swap values.
output = ""
idx = {"0":"0","1":"T","T":"1"}
if sign == -1:
    output = "".join([idx[i] for i in out[::-1]])

# Print correct balanced ternary.
if begin==0:
    print("0")
else:
    print(out[::-1] if output=="" else output)
