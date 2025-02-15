# Hashmap for storing parts of the ship.
ship_components = {"#"=>"Block","^"=>"Thruster","@"=>"Gyroscope","+"=>"Fuel","§"=>"Core"}

# Get ship dimension and rotation.
x = gets.to_i
y = gets.to_i
r = gets.to_i

# Form ship - Only relevant components.
ship = ""
y.times do
  ship += gets.chomp.chars.select{|i| ship_components.has_key?(i)}.join
end

# Rotate ship if required.
ship = ship.reverse if r == 1
  
# Variable required.
out = []
prev = ""
j = 0

# Perform RLE on the data with only interest in the ship components
while j < ship.size do
  count = 1
  prev = ship[j]
  j+=1
  while j < ship.size && ship[j] == prev do
    count+=1 if ship[j] == prev
    j += 1
  end

  if ship_components.has_key?(prev)
    plural = count > 1 ? "s" : ""
    out << [[count.to_s , ship_components[prev] + plural].join(" ")]
  end
end

# Print the ship contents if a ship if found, otherwise 'Nothing'.
if out.size > 0
    puts out.join(", ")
else
    puts "Nothing"
end
