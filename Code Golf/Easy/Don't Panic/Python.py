I=input
N=int
*_,y,x,_,_,n=[N(i)for i in I().split()]
e=sorted([[N(j)for j in I().split()]for _ in"1"*n]+[[y,x]])
while 1:j,k,d=I().split();j,k=N(j),N(k);d=d[0];f=e[j][1];print(["WAIT","BLOCK"][k<f and d=="L"or k>f and d=="R"])
