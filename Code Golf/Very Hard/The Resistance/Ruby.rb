m=gets.chop
w=[]
gets.to_i.times{w<<gets.chomp.chars.map{|c|Hash[('A'..'Z').zip %w[.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..]][c]}.join}
c={}
s=->(i,m,w,c){return 1if i==m.size;return c[i]if c[i];t=0;w.each{|x|t+=s[i+x.size,m,w,c]if m[i,x.size]==x};c[i]=t}
p s[0,m,w,c]
