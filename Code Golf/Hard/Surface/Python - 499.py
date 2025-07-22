from collections import deque
I=input
G=[]
l=int(I())
h=int(I())
for i in range(h):G+=[list(I())]
def S(y,x, V):
 Q=deque([[y,x]])
 while Q:
  y,x=Q.popleft()
  for Y,X in[(1,0),(0,1),(-1,0),(0,-1)]:
   Y=Y+y;X=X+x
   if(Y,X) not in V and 0<=Y<h and 0<=X<l and G[Y][X]=="O":V.add((Y,X));Q.append([Y,X])
 s=len(V)
 for y,x in list(V):G[y][x]=s
 return s
for i in " "*int(I()):
 x,y=[int(j)for j in I().split()]
 if G[y][x]=="#":print(0)
 elif G[y][x] != "O":print(G[y][x])
 else:print(S(y,x,{(y,x)}))
