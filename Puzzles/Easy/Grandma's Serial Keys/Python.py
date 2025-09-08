# Get name.
name = input()

# Get value.
sum_val = sum(ord(i) for i in name)
seed = (len(name) * sum_val) ^ 20480 

# Get segment values.
s1 = seed & 65535
s2 = seed >> 16
s3 = len(name) * (ord(name[0])+ ord(name[-1]))
s4 = (s1+s2+s3) % 65536

# Print the key.
def c(number):
    return hex(number)[2:].rjust(4,"0").upper()
print(f"{c(s1)}-{c(s2)}-{c(s3)}-{c(s4)}")
