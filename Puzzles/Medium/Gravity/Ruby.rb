# Get counts of number of # per column.
width, height = gets.split.map { |x| x.to_i}
counts = width.times.map{|x| 0}
height.times do
  line = gets.chomp
  line.chars.each.with_index do |char , i|
    counts[i] += 1 if char == "#"
  end
end

# Print each row after gravity effects.
(1..height).each do |h|
  h = height - h
  row = []
  counts.each{|val| row << (val > (h) ? "#" : ".")}
  puts row.join
end
