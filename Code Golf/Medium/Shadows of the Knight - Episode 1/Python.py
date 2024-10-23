I=input
w,h,_,x,y=[int(i)for i in I().split()+[I()]+I().split()]
X=Y=0
while d:=I():
 if"U"in d:h=y-1
 if"D"in d:Y=y+1
 if"L"in d:w=x-1
 if"R"in d:X=x+1
 print(x:=(X+w)//2,y:=(Y+h)//2)
