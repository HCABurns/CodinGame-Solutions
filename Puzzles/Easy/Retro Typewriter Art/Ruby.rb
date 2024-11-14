# Create hashmap for special characters, and set for numbers.
special_character_hashmap = {"sp"=>" ", "bS"=>"\\", "sQ"=>"'", "nl"=>"\n"}
numbers_set = ["1","2","3","4","5","6","7","8","9","0"]

gets.chomp.split.each{|i|
    # Check if all numbers in input. If so then output.
    i[0,i.size-1].to_i.times{print i[i.size-1,1].to_i} if i == i.to_i.to_s

    # Split the input into numbers and characters. (quantity minimum 1)
    quantity = [i.chars.select{|j| numbers_set.include?(j)}.join.to_i,1].max
    string = i.chars.select{|j| !numbers_set.include?(j)}.join

    # Print correct char * quantity (Replace special characters with char in hashmap)
    o=""
    if special_character_hashmap[string]
        o=special_character_hashmap[string]*quantity
    else
        o=string*quantity
    end
    # Output the string.
    print o
    #end
}
