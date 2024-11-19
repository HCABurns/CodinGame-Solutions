# Get text to decode.
text_to_decode = input()

# Caeser shift through all range until CHIEF is found or no more shifts to occur.
for shift in range(-26,26):
    shifted = ""
    for char in text_to_decode:
        if char.isalpha():
            char = chr(ord("A") + (ord(char) - ord("A") - shift)%26)
        shifted += char

    # If chief is found, print plaintext and quit.
    if "CHIEF" in shifted.split(" "):
        print(shifted)
        quit()

# If CHIEF not found, print "WRONG MESSAGE"
print("WRONG MESSAGE")
