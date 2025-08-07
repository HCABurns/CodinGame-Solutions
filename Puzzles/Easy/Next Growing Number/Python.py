# Get value and convert to string of value+1.
k = input()
n = [int(i) for i in str(int(k)+1)]

# Convert to next growing number.
l = 1
bigger = False
while l < len(n):
    if n[l] < n[l-1]:
        n[l] = n[l-1]
        
    if l < len(k) and int(k[l-1]) < n[l-1]:
        bigger = True
        
    if bigger:
        n[l] = n[l-1]
    
    l += 1

# Print next growing number.
print("".join([str(i) for i in n]))
