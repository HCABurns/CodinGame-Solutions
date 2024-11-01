# Get values to be used to find GCD.
a, b = gets.split.map { |x| x.to_i }
a_start , b_start = a,b

#  Continue until remainder is 0.
while b!=0 do
    puts "#{a}=#{b}*#{a/b}+#{a%b}"
    tmp = a%b
    a = b
    b = tmp
end

# Output the GCD of a and b.
puts "GCD(#{a_start},#{b_start})=#{a}"
