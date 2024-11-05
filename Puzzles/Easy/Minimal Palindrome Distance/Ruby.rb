# Get input string and length.
n = gets.to_i
s = gets.chomp

#Find Longest palindrome starting from the back.
longest = 1
(0..n-1).each do |j|
    if s[n-1-j,j+1] == s[n-1-j,j+1].reverse && j>longest
        longest = j + 1
    end
end

# Print number of chars that need to be added from the front to make a palindrome.        
puts n - longest
