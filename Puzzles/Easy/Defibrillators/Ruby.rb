include Math

# Convert longitude and latitude to float values.
lon = gets.chomp.tr(',', '.').to_f
lat = gets.chomp.tr(',', '.').to_f

# Create array for storing values.
out = []

# Go through each input, storing the distance and the name.
n = gets.to_i
n.times do
  defib = gets.chomp
  s = defib.split(';')
  defib_lon = s[-2].tr(',', '.').to_f
  defib_lat = s[-1].tr(',', '.').to_f

  x = (defib_lon - lon) * cos((defib_lon + lon) / 2 * PI / 180)
  y = defib_lat - lat
  d = sqrt(x**2 + y**2) * 6371

  out << [d, s[1]]
end

# Find the closest value and output the name.
puts out.min_by{|d, _| d}[1]
