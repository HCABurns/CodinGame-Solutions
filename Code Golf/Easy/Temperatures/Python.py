m=input
print(sorted([(-i*i,i)for i in map(int,m().split())])[-1][1])
