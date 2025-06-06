s={}
gets.to_i.times{t=gets.chop;t.size.times{|z|s[t[..z]]=1}}
p s.size
