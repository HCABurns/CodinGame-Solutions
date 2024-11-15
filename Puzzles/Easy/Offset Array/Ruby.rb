# Form hashmap of hashmaps using given ranges and values.
maps = {}
n = gets.to_i
n.times do
  r , vals = gets.chomp.split("=")
  idx , ra = r.split("[")
  ra , _ = ra.split("]")
  lb , _ , rb = ra.split(".") 
  vals = vals.strip.split(" ")
  maps[idx] = {}
  (lb.to_i..rb.to_i+1).zip(vals).each{|j , val|maps[idx][j.to_s] = val}
end

# Get inputs and convert to only useful information. Val is starting index, stack is order of searching.
stack = gets.chomp
val = stack.chars.select{|i| i.match(/[\d-]/)}.join
stack = stack.tr(val , "").split("[").reverse

# Find and print value using maps.
stack[1..].each{|idx| val = maps[idx][val]}
puts val
