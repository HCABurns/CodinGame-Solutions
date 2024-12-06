# Arrays for storing information.
planets = []
alice = []

# Get all inputs, calculate density and store required information.
n = gets.to_i
n.times do
  # Get inputs.
  name, r, m, c = gets.split

  # Convert to float.
  r, m, c = [r,m,c].map(&:to_f)

  # Set planet details to correct location.
  if name == "Alice"
    alice = [r , (m/((4/3)*Math::PI*r**3))]
  else
    planets << [c, r, (m/((4/3)*Math::PI*r**3)), name]
  end
end

# Sort based on distance.
planets = planets.sort

# Print the closest planet name that will not be disintergrated by Alice.
planets.each do |i|
  v = (2 * alice[1] / i[2])
  roche = alice[0] * v**(1.0/3.0)
  #p roche
  if i[0] >= roche
    puts i[-1]
    break
  end
end
