# Get width and height of input.
w, h = gets.split.map { |x| x.to_i }

# Create output array
out = []

# Keep adding LSD onto out until it's length is 8. Then convert and print.
h.times do
  inputs = gets.split
  for j in 0..(w-1)
    pixel = inputs[j].to_i
    out << pixel.to_s(2)[-1].to_s
    # If output is 8 bits, convert to ASCII char and print. Also clear array.
    if out.size == 8
      print out.join.to_i(2).chr
      out = []
    end
  end
end
