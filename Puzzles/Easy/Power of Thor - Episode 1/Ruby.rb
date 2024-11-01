STDOUT.sync = true # DO NOT REMOVE

# Get inputs.
light_x, light_y, thor_x, thor_y = gets.split.map { |x| x.to_i }

# Loop and if thor needs to move a direction, append it to output.
loop do
  remaining_turns = gets.to_i # The remaining amount of turns Thor can move. Do not remove this line.
  output=""
  # If thor is below light, move north.
  if light_y < thor_y
      output="N"
      thor_y-=1
  end
  # If thor is above light, move south.
  if light_y > thor_y
      output="S"
      thor_y+=1
  end
  # If thor is right of the light, move west.
  if light_x < thor_x
      output+="W"
      thor_x+=1
  end
  # If thor is left of the light, move east.
  if light_x > thor_x
      output+="E"
      thor_x-=1
  end
  puts output
end
