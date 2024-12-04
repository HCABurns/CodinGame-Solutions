# Get information.
small_radius, large_radius, glass_height, beer_vol = gets.split.map { |x| x.to_f }

# Get starting height
test_height = 0.0001
current_volume = 1e9

# Continue until volume at test height is within 0.1 of the beer height
while (current_volume - beer_vol).abs > 0.1
    # Calculate large_radius at the current height h
    test_large_radius = small_radius + (large_radius - small_radius) * (test_height / glass_height)
    
    # Calculate the volume up to height h
    current_volume = (Math::PI * test_height / 3) * (small_radius**2 + small_radius * test_large_radius + test_large_radius**2)
    
    # Increment test height
    test_height += 0.0001
end

# Print height that the liquid reaches
puts test_height.round(1)
