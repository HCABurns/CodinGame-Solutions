# Get Hashmap of angles and directions.
angles = {"N"=>0,"NE"=>45,"E"=>90,"SE"=>135,"S"=>180,"SW"=>225,"W"=>270,"NW"=>315}
directions = {"RIGHT"=>45,"LEFT"=>-45,"FORWARD"=>0,"BACK"=>180}

# Get starting direction.
start_direction = gets.chomp
direction = angles[start_direction]

# Simulate moves.
n = gets.to_i
n.times do
  turn = gets.chomp
  direction = (direction + directions[turn]) % 360
end

# Output the angle the person is facing.
angles.each do |key , angle|
  if angle == direction
    puts key
  end
end
