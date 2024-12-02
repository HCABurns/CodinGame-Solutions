# Get input and convert.
line_1 = input()
line_2 = input()
line_3 = input()
key = (line_1+"\n"+line_2+"\n"+line_3).split("\n")

# Hashmap for converting to value.
converter = {" _ | ||_|":"0","     |  |":"1"," _  _||_ ":"2"," _  _| _|":"3","   |_|  |":"4"," _ |_  _|":"5"," _ |_ |_|":"6"," _   |  |":"7"," _ |_||_|":"8"," _ |_| _|":"9"}

# Convert each number to value.
for i in range(0,(len(line_1)*3) // 3,3):
    top = key[0][i:i+3]
    mid =  key[1][i:i+3]
    bot = key[2][i:i+3]
    print(end = converter[top+mid+bot])
