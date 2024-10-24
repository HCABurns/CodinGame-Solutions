I=input
n=int(I());s,u=zip(*(map(int,I().split())for _ in[0]*n))
u=sorted(u);I(sum(abs(u[n//2]-v)for v in u)+max(s)-min(s))
