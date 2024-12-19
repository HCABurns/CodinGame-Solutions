# Get number.
n = gets.to_i

# Set values.
t = 5
pk = 2
k = 3

# Find combinations.
combs = []
(0...(n/t).floor + 1).each do |a|
    (0...[(n/pk).floor + 1, a+1].min).each do |b|
        (0...(n/k).floor + 1).each do |c|
            total = a*t + b*pk + c*k
            break if total > n
            if total == n
                combs << [a, b, c] if !combs.include?([a, b, c])
            end
        end
    end
end

# Sort and display results
combs.each do |comb|
    puts "#{comb[0]} #{comb[1]} #{comb[2]}"
end
