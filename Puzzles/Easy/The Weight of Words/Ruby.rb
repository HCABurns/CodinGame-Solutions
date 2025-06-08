# Get required inputs
steps = gets.to_i
h = gets.to_i
width = gets.to_i
rows = []
w = []
h.times do
  rows << gets.chomp
end

steps.times do
  # Convert rows to columns
  columns = rows.map(&:chars).transpose

  # Column weights and shifts
  w2 = columns.map { |col| col.sum(&:ord) }
  columns.each_with_index do |col, i|
    shift = w2[i] % h
    columns[i] = col.rotate(-shift)
  end

  # Rebuild rows from shifted columns
  rows = columns.transpose.map(&:join)

  #Calculate new row weights
  w = []
  rows.each do |row|
    w << row.each_char.map{|c| c.ord}.sum
  end

  #Move the rows by X amount
  w.each_with_index do |weight, i|
    (weight%width).times do 
      rows[i] = rows[i][-1] + rows[i][0,rows[i].size-1]
    end
  end
end

#Output the rows
(0...h).each do |i|
  puts rows[i]
end
