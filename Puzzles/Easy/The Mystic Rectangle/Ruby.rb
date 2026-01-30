# Get inputs.
x, y = gets.split.map { |x| x.to_i }
u, v = gets.split.map { |x| x.to_i }

# Calcualte shortest distance.
dx = [(x-u).abs,200-(x-u).abs].min
dy = [(y-v).abs,150-(y-v).abs].min
ddiag = [dx,dy].min

# Calculate time.
t = ddiag*0.5
t += (dx-ddiag)*0.3
t += (dy-ddiag)*0.4

# Print time.
puts t.round 1
