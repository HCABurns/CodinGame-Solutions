# Form Grid
grid = []
25.times do
  row = []
  19.times do
    row << "{}"
  end
  grid << row
end

# Perform the instructions of mowing, plating or plant and mowing on the grid.
gets.chomp.split.each do |instruction|
    radii = instruction.chars.select { |char| char.match?(/\d/) }.join.to_f / 2
    chars = instruction.chars.select { |char| char.match?(/[a-zA-Z]/) }
    j, i = chars[-2].ord - "a".ord, chars[-1].ord - "a".ord
    symbol = nil
    if instruction.include?("PLANTMOW")
        symbol = nil
    elsif instruction.include?("PLANT")
        symbol = "{}"
    else
        symbol = "  "
    end

    # Complete operation on any value inside the given circle.
    rounded_radii = radii.ceil
    ([0,i-rounded_radii].max ... [grid.size,i+rounded_radii].min).each do |y|
        ([0,j-rounded_radii].max ... [grid[0].size,j+rounded_radii].min).each do |x|
            dist = ((y-i)**2 + (x-j)**2)**0.5
            if dist <= radii
                if symbol == "  " || symbol == "{}"
                    grid[y][x] = symbol
                else
                    grid[y][x] = grid[y][x] == "{}" ? "  " : "{}"
                end
            end
        end
    end

end

# Output the crop circle.
grid.each{|row| puts row.join}
