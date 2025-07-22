from collections import deque
Q=deque([])
l,c,n=[int(i)for i in input().split()]
for i in range(n):Q.append([int(input()),i])
C={}
T=r=D=F=0
t={0:0}
while c>0:
 if D in C:
  if F<1:l=r-C[D][2];a=c//l;g=T-t[C[D][2]];T+=g*a;c%=l;F=1
  if c>0:c-=1;T+=C[D][0];D=C[D][1]
 else:
  y=o=0;x=[]
  while Q[0][0]+y<=l and Q[0][1] not in x:V,X=Q.popleft();y+=V;Q.append([V,X]);o+=V;x+=[X]
  T+=o;C[D]=[o,(x[-1]+1)%n,r];D=(x[-1]+1)%n;r+=1;t[r]=T;c-=1
print(T)
