c=o=[]
I=input
l,h=map(int,I().split())
for _ in" "*h:
 V=I();v=len(V);j=0
 while j<v:
  if len(c)!=v//l:c+=[[]]
  c[j//l]+=[V[j:j+l]];j+=l
Z=[0,0]
for i in[0,1]:
 for v in range(int(I())//l,0,-1):Z[i]+=(c.index([I()for _ in" "*h]))*(20**(v-1))
r=int(eval(f"{Z[0]}{I()}{Z[1]}"))
if r<1:o=[0]
while r>0:o=[r%20]+o;r//=20 
for v in o:print(*[n for n in c[v]],sep="\n")
