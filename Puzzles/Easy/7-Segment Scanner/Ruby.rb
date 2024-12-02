# Get input and convert.
line_1 = gets.chomp
line_2 = gets.chomp
line_3 = gets.chomp
key = (line_1+"\n"+line_2+"\n"+line_3).split("\n")

# Hashmap for converting to value.
converter = {" _ | ||_|"=>"0","     |  |"=>"1"," _  _||_ "=>"2"," _  _| _|"=>"3","   |_|  |"=>"4"," _ |_  _|"=>"5"," _ |_ |_|"=>"6"," _   |  |"=>"7"," _ |_||_|"=>"8"," _ |_| _|"=>"9"}

# Convert each number to value.
(0..(line_1.size/3).floor).each do |i|
    top = key[0][i*3,3]
    mid =  key[1][i*3,3]
    bot = key[2][i*3,3]
    print converter[top+mid+bot]
end
