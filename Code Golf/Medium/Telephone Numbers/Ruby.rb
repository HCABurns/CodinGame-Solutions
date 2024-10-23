s=[]
gets.to_i.times{t=gets.chomp;[*0..t.size].each{|z|s<<t[..z]}}
p s.uniq.size
