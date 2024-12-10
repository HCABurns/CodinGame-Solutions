l,c=map(int,input().split())
g=[list(input())for _ in l*" "]
i=j=Q=D=V=B=C=f=0;t=[]
for r in g:
 J=0
 for v in r:
  if v=="@":i,j=Q,J
  if v=="T":t+=[(Q,J)]
  J+=1
 Q+=1
d={"N":2,"S":0,"E":1,"W":3}
m=[(1,0),(0,1),(-1,0),(0,-1)]
if t:t={t[0]:t[1],t[1]:t[0]}
v=[]
while(i,j,D,V,B,C)not in v:
 v+=[(i,j,D,V,B,C)]
 if g[i][j]=="$":f=1;break
 if g[i][j]in d:D=d[g[i][j]]
 if g[i][j]=="I":V^=1
 if g[i][j]=="B":B^=1
 if g[i][j]=="T":i,j=t[(i,j)]
 N=-1if not V else 4
 while 1:
  I,J=i+m[D][0],j+m[D][1]
  if 0<=I<l and 0<=J<c and g[I][J]!="X"and g[I][J]!="#"or g[I][J]=="X"and B and l-1!=I!=0 and c-1!=J!=0:
   if g[I][J]=="X"and B:g[I][J]=" ";C+=1
   i,j=I,J;break
  else:N-=1if V else-1;D=N%4
print("\n".join(["SOUTH","EAST","NORTH","WEST"][d[2]]for d in v[1:])if f else"LOOP")
