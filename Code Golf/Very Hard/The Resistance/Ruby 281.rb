m=gets.chop
w=[]
gets.to_i.times{w<<gets.bytes.map{|z|%w[.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..][z-65]}.join}
c={m.size=>1}
s=->(i){return c[i]if c[i];t=0;w.each{|x|t+=s[i+x.size]if m[i,x.size]==x};c[i]=t}
p s[0]
