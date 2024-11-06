I=input
m=I()
c={len(m):1}
w=["".join(map(lambda x:{chr(c):m for c,m in zip(range(65,91),".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split(" "))}[x],[*I()]))for _ in['']*int(I())]
def f(i):
 if i in c:return c[i]
 t=sum(f(i+len(x))for x in w if m[i:i+len(x)]==x)
 c[i]=t
 return t
I(f(0))
