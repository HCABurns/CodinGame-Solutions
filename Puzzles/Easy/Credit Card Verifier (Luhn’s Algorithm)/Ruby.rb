# Get number of cards to check
n = gets.to_i

arr = []
n.times do
  # Get card number,remove spaces and convert to integer.
  card = gets.chomp
  card = card.gsub(/\s+/, "")
  arr = card.each_char.map{|x| x.to_i}
  
  # Step 1 and 2
  sum_val = 0
  arr.reverse.select.with_index do |value,i|
    if i % 2 == 1
      if value*2 < 10
        sum_val += value*2
      else
        sum_val += (value*2)-9
      end
    end
  end

  #Step 3
  odd_sum = 0
  arr.select.with_index do |value,i|
    odd_sum += value if i%2==1
  end

  if (sum_val + odd_sum) % 10 == 0
    puts "YES"
  else
    puts "NO"
  end
end
