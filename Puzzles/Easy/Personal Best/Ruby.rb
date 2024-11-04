# Form hashamps and arrays to be used.
gymnasts = gets.chomp.split(",")
cats = ["bars","beam","floor"]
categories = gets.chomp.split(",").map{|category| cats.index(category)}
athletes = {}

# Get max scores of gymnasts and store in hashmap.
n = gets.to_i
n.times do
  name,bars,beam,floor = gets.chomp.split(",")
  if !athletes.include?(name)
      athletes[name] = [bars,beam,floor]
  else
    bars_pr, beam_pr, floor_pr = athletes[name]
    athletes[name] = [[bars,bars_pr].max,[beam,beam_pr].max,[floor,floor_pr].max]
  end
end

# Output scores of gymnasts in given categories.
gymnasts.each do |name|
  output = []
  categories.each do |idx|
    output << athletes[name][idx]
  end
  puts output.join(",")
end
