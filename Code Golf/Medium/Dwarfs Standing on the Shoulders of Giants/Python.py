h={}
for i in " "*int(input()):
 x,y=input().split()
 if x not in h:h[x]=[]
 h[x]+=[y]
def f(n):
 c=h.get(n,[]);l=1
 for i in c:
  if r:=f(i):l=max(l,r+1)
 return l
print(max(f(i)for i in h))
