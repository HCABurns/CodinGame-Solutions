# Create empty grid.
out = []
4.times{out << [] ; 6.times{out[-1] << "_____"}}

# Get times.
timer = gets.chomp.split(":")
idx = 0
4.times do |i|
  # Get digits if possible.
  t1 = timer[i].size == 1 || i == 0 ? timer[i].to_i : timer[i][0].to_i
  t2 = timer[i].size > 1 && i != 0 ? timer[i][1].to_i : nil

  # Convert to binary.
  t1_binary = t1.to_s(2).rjust(4, "0")
  t2_binary = t2 ? t2.to_s(2).rjust(4, "0") : nil

  # Convert any 1s to "#####". Use idx to place into correct column.
  t1_binary.chars.each_with_index do |val, j|
    out[j][idx] = "#####" if val == "1"
  end
  idx += 1

  if t2_binary
    t2_binary.chars.each_with_index do |val, j|
      out[j][idx] = "#####" if val == "1"
    end
    idx += 1
  end
end

# Output Binary Coded Decimal Clock
out.each{|row|puts "|"+row.join("|")+"|"}
