a,b,x,y=map(int,input().split())
while 1:print((" NS"[(b>y)+(b!=y)]+" WE"[(a>x)+(a!=x)]).strip());x+=a>x;y+=b>y
