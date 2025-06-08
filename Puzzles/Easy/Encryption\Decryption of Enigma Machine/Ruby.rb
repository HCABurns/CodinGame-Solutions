#Get required inputs
operation = gets.chomp
pseudo_random_number = gets.to_i

#Get rotors and store in array.
rotors = []
3.times do
  rotors << gets.chomp
end

#Get message
message = gets.chomp

#If Encode then encode
if operation=="ENCODE"
  s = []
  message.each_char do |char|
    #Add pseudo_random_number to current character - IF required wrap value.
    val = char.ord + pseudo_random_number
    if val>"Z".ord
      val = "A".ord + (val - "A".ord)%26
    end
    s << val.chr
    #Increment pseudo_random_number
    pseudo_random_number += 1
  end
  #Form message and rotate
  message = s.join
  rotors.each do |rotor|
    arr = []
    message.each_char do |i|
      arr << rotor[i.ord-"A".ord]
    end
    message=arr.join
  end
#If decode then decode - Reverse of encoding - Rotate first then shift
else
  #Complete backwards rotations with rotors
  L="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  rotors.reverse.each do |rotor|
    s = []
    message.each_char do |i|
      s << L[rotor.index(i)]
    end
    message=s.join
  end
  #Shift values using pseudo_random_number
  s = []
  message.each_char do |char|
    val = char.ord - pseudo_random_number
    if val<"A".ord
        val = "A".ord + ((val - "A".ord)%26)
    end
    s << val.chr
    pseudo_random_number += 1
  end
  message = s.join
end
    
#Output the encoded/decoded message
puts message
