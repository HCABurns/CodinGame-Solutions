n=int(input());s=[];u=[]
for _ in"1"*n:x,y=map(int,input().split());s+=[x];u+=[y]
u.sort()
print(sum(abs(u[n//2]-v)for v in u)+max(s)-min(s))
