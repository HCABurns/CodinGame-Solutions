o,b=""
gets.chomp.chars{|c|('%07b'%c.ord).chars{|i|o+=i==b ?'0':[" 00 0"," 0 0"][i.to_i];b=i}}
puts o.strip
