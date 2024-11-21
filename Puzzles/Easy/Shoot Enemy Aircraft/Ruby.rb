# Get planes locations and position of SAM launcher.
pos = []
planes = []

n = gets.to_i
n.times do |i|
  gets.chomp.chars.each.with_index do |char, j|
    if "<>".include? char
      planes << [i, j]
    elsif "^" == char
      pos = [i+1, j]#NOTE:+1 As missle travels from launcher location.
    end
  end
end

# Continue until all planes have been shot down.
while planes.size > 0
  # Define boolean if a shot is to be taken or not.
  shoot = false

  # Plane to be remove
  to_remove = nil

  # Move plane and check if they can be shot.
  planes.each do |plane|
    y , x = plane
    # Check if vertical distance between plane and SAM equals horizontal distance between.
    # If so then they will intercept so shoot.
    if (x-pos[1]).abs == (pos[0] - y)
      to_remove = plane
      shoot = true
    else
      # Move plane.
      if x < pos[1]
        plane[1] += 1
      else
        plane[1] -= 1
      end
    end
  end
  
  # Remove plane if shot.
  #NOTE: Delete takes last index - index takes the first - Use index and delete at that index.
  planes.delete_at(planes.index(to_remove)) if to_remove != nil
  
  # Output if a shot has been taken or not.
  puts shoot == true ? "SHOOT" : "WAIT"
end
