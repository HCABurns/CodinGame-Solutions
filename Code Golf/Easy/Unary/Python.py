o=""
p=2
for c in input():
 for i in'{:07b}'.format(ord(c)):o+=[[" 00 0"," 0 0"][int(i)],"0"][i==p];p=i
print(o[1:])
