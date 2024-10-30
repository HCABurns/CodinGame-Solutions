o,b=""
gets.chomp.each_char{|c|('%07b'%c.ord).each_char{|i|o+=i==b ?'0':[" 00 0"," 0 0"][i.to_i];b=i}}
puts o.strip
