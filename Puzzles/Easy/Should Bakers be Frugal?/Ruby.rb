# Get length of dough and size of circle.
side, diameter = gets.split.map { |x| x.to_f }

# Calculate wasteful bakers amount.
wasteful = (side / diameter).floor ** 2

# Calculate frugal bakers amount.
frugal = 0
area = side**2
while side > diameter
    # Calculate amount possible to be cut.
    amount = ((side/diameter).floor**2)
    frugal += amount

    # Convert wasted into a new dough rectangle.
    area -= amount * (Math::PI*(diameter/2)**2)
    side = area ** 0.5
end

# Output the difference between frugal and wasteful.
puts frugal-wasteful
