I=input
c={len(m:=I()):1}
w=["".join(map(lambda x:{chr(c):m for c,m in zip(range(65,91),".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split())}[x],[*I()]))for _ in' '*int(I())]
def f(i):
 if i in c:return c[i]
 c[i]=sum(f(i+len(x))for x in w if m[i:i+len(x)]==x);return c[i]
I(f(0))
