# Get ciphertext to be decoded.
text_to_decode = gets.chomp

# Caeser shift through all range until CHIEF is found or no more shifts to occur.
(0..26).each do |shift|
  shifted = ""
  text_to_decode.chars.each do |char|
    if char.match?(/[A-Za-z]/)
      shifted += ("A".ord + (char.ord - "A".ord - shift)%26).chr
    else
      shifted += char
    end
  end
  # If chief is found, print plaintext and quit.
  if shifted.split(" ").include?("CHIEF")
    print(shifted)
    exit()
  end
end
# If CHIEF not found, print "WRONG MESSAGE"
print("WRONG MESSAGE")
