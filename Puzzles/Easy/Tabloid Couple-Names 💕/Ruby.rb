# Get number of couples.
n = gets.to_i

# Find tabloid Couple-Names.
n.times do
  # Get both names.
  a_couple = gets.chomp.split
  name1, name2 = a_couple[0] , a_couple[2]

  # Convert to lower for comparisions.
  n1 = name1.downcase
  n2 = name2.downcase
  
  # Find overlapping substrings.
  n1s = []
  overlaps = []
  (0..n1.size-1).each do |idx|
    (0..n1.size-idx).each do |i|
      n1s << n1[idx,i]  if n1[idx,i] != ""
    end
  end
  (0..n2.size-1).each do |idx|
    (0..n2.size-idx).each do |i|
      overlaps << n2[idx,i] if n1s.include?(n2[idx,i]) && !overlaps.include?(n2[idx,i])
    end
  end

  # Find all possible tabloid names.
  words = []
  overlaps.each do |overlap|
    [[n1, n2], [n2, n1]].each do |n1, n2|
      (0..(n1.size - overlap.size)).each do |w1_idx|
        if n1[w1_idx, overlap.size] == overlap
          (0..(n2.size - overlap.size)).each do |w2_idx|
            if n2[w2_idx, overlap.size] == overlap
              words << [(n1[0,w1_idx + overlap.size] + n2[w2_idx + overlap.size..-1]), overlap.size]
            end
          end
        end
      end
    end
  end

  # Find only valid words, then select all those names with max number of overlapping characters.
  words = words.uniq
  words = words.select{ |i,v| !n1.include?(i) && !n2.include?(i) && i.size >= [n1.size,n2.size].min}
  
  if words.size > 0
    max_v = words.max_by{|_,v| v}[1]
    words = words.select{|i,v| v == max_v}
  end
  # Print names or None if no valid tabloid names.
  puts "#{name1} plus #{name2} = #{words.size > 0 ? words.map{|i,_| i.capitalize}.sort.join(" ") : 'NONE'}"
end
