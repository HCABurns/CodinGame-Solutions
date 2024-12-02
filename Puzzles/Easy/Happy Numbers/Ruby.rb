# Get inputs.
n = gets.to_i
n.times do
  x = gets.chomp.to_i
  start_value = x

  # Find if x is happy or not.
  seen = []
  while !seen.include?(x) && x != 1 do
    seen << x
    val = 0
    while x > 0 do
      val += (x%10)**2
      x = (x / 10).floor
    end
    x = val

  end

  # Print correct face depending on if x is happy or not.
  if seen.include?(x)
    puts start_value.to_s + " :("
  else
    puts start_value.to_s + " :)"
  end
end
