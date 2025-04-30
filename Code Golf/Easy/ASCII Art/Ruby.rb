l=gets.to_i
gets
t=gets.chop.upcase
$<.each_line{|r|puts t.chars.map{|c|r[(c.ord<65?26:c.ord-65)*l,l]}.join}
