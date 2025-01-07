# Define points and drivers array.
points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
drivers = []

# Get drivers names and points tally.
n = gets.to_i
n.times do
  name, results = gets.chomp.split(":")
  total = 0
  results.split(" ").each do |i|
    res = i.chars.select { |j| j =~ /[0-9]/ }.join
    res = res.empty? ? 11 : res.to_i
    if res <= 10
      total += points[res - 1] + (i.include?("F") ? 1 : 0)
    end
  end

  drivers << [total, name]
end

# Sort on points.
drivers.sort_by! { |driver| -driver[0] }

# Print drivers names.
drivers.each do |_, name|
  puts name
end
