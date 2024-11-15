# Get height of the grid.
height = gets.to_i

# Get first row, get number of activities and attendees.
line1 = gets.chomp.split(":")
grids_counter = line1.size
scores = [[]]
line1.each{|quad| scores[0] << quad.count("*")}
t = scores[0].sum.to_f
quadrant = 0

# Go through grid and get attendees and store in correct position.
(height-1).times do
  row = gets.chomp
  if row.include?("+")
    scores << []
    grids_counter.times{scores[-1] << 0}
    quadrant += 1
  else
    
    # Get count for that activity and add to scores array.
    row.split(":").each.with_index do |activity , j |
      count = activity.count("*")
      t += count
      scores[-1][j] = scores[-1][j] + count
    end
  end
end

# Output the total attendees and percentages of attendees for each activity.
puts "#{t.to_i} attendees"
scores.each do |row|
  puts row.map {|i|"#{(i/t*100).round.to_s.rjust(3, '_')}%"}.join(" ")
end
