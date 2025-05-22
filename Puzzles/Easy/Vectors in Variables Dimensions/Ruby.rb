# Array for storing coordinates.
coordinates = []

# Read in the coordinates and store.
d = gets.to_i
n = gets.to_i
n.times do
  point = gets.chomp
  name, pos = point.split("(")
  pos = pos[0,pos.size-1].split(",")
  coordinates << [name, pos.map(&:to_i)]
end

# Compare all the vectors storing distance with the information about the vector.
vectors = []
(0...coordinates.size).each do |i|
  name1, pos1 = coordinates[i]
  (i+1...coordinates.size).each do |j|
    name2, pos2 = coordinates[j]
    dist = 0
    dists = []
    pos1.zip(pos2).each do |v1, v2|
      dist += (v1-v2)**2
      dists << (v2-v1).to_s
    end
    vectors << [dist,name1+name2+"("+dists.join(",")+")"]
  end
end

# Sort the vectors and print the shortest and largest.
vectors = vectors.sort_by{|dist,_| dist}
puts (vectors[0][1])
puts (vectors[-1][1])
