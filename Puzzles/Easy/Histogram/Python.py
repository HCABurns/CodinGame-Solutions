# Get inputs.
s = input().upper()

# Find the frequencies and convert to percentage for all alphabetical characters.
chars = {i:s.count(i) for i in s if i.isalpha()}
chars_count = sum([v for v in chars.values()])
chars = {i:round(float(v)/chars_count*100,2) for i,v in chars.items()}

# Print out the histogram. (0.1 added required as python bankers rounding causes wrong result)
for i in range(0,26):
    char = chr(ord("A")+i)
    size = round(chars.get(char,0)+0.1)
    if i == 0:print("  +"+ "-"*size + ["+" if size > 0 else ""][0])
    print(char+ " " + ["","|"][size != 0] + " "*size + f"|{chars.get(char,0):.2f}%")
    
    m = round(chars.get(char,0)+0.1)
    n = round(chars.get(chr(ord(char)+1),0)+0.1)

    size = round(max(chars.get(char,0), chars.get(chr(ord(char)+1),0))+0.1)
    f = [i for i in "  +"+ "-"*size + ["+" if size > 0 else ""][0]]
    
    if m != 0: f[m+3] = "+"
    if n != 0: f[n+3] = "+"

    print("".join(f))
    
