c=o=[]
I=input
l,h=map(int,I().split())
for _ in " "*h:
 V=I()
 for j in range(0,len(V),l):
  if len(c)!=len(V)//l:c+=[[]]
  c[j//l]+=[V[j:j+l]]
n=N=0
for v in range(int(I())//l,0,-1):N+=(c.index([I()for _ in" "*h]))*(20**(v-1))
for v in range(int(I())//l,0,-1):n+=(c.index([I()for _ in" "*h]))*(20**(v-1))
r=int(eval(f"{N}{I()}{n}"))
if r==0:o=[0]
while r>0:o=[r%20]+o;r//=20 
for v in o:print(*[n for n in c[v]],sep="\n")
