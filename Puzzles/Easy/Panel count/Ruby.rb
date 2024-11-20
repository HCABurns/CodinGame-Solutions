# Define empty array of people.
people = []

# Get property list.
properties = gets.to_i.times.map{gets.chomp}

# Form hahsmaps of people containing properties and value.
gets.to_i.times do
  people << {}
  _ , *info = gets.chomp.split
  properties.zip(info).each{|prop , data| people[-1][prop] = data}
end

# Get criteria to be used searched.
criteria = gets.to_i.times.map{gets.chomp}

# Search every person against the criteria and print number of people who satisfy the criteria.
criteria.each do |formula|
  total = 0
  people.each do |info|
    valid = true
    formula.split("AND").each do |data|
      prop , val = data.strip().split("=")
      if info[prop] != val
        valid = false
        break
      end
    end
    total += 1 if valid
  end
  p total
end
