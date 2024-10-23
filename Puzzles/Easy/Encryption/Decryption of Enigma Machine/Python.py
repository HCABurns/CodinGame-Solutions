#Get required inputs
operation = input()
pseudo_random_number = int(input())

#Get rotors and store in array.
rotors = [input() for i in range(3)]

#Get message
message = input()

#If Encode then encode
if operation=="ENCODE":
    s = []
    for char in message:
        #Add pseudo_random_number to current character - IF required wrap value.
        val = ord(char) + pseudo_random_number
        if val>ord("Z"):
            val = ord("A") + (val - ord("A"))%26
        s.append(chr(val))
        #Increment pseudo_random_number
        pseudo_random_number += 1
    #Form message and rotate
    message = "".join(s)
    for rotor in rotors:
        message="".join([rotor[ord(i)-ord("A")] for i in message])
#If decode then decode - Reverse of encoding - Rotate first then shift
else:
    #Complete backwards rotations with rotors
    L="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for rotor in rotors[::-1]:
        s=[L[rotor.index(i)] for i in message]       
        message="".join(s)
    #Shift values using pseudo_random_number
    s = []
    for char in message:
        val = ord(char) - pseudo_random_number
        if val<ord("A"):
            val = ord("A") + ((val - ord("A"))%26)
        s.append(chr(val))
        pseudo_random_number += 1
    message = "".join(s)

#Output the encoded/decoded message
print(message)
