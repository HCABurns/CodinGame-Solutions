# Get hex of chars.
chars = "0x1818243C42420000, A, 0x7844784444780000, B, 0x3844808044380000, C, 0x7844444444780000, D, 0x7C407840407C0000, E, 0x7C40784040400000, F, 0x3844809C44380000, G, 0x42427E4242420000, H, 0x3E080808083E0000, I, 0x1C04040444380000, J, 0x4448507048440000, K, 0x40404040407E0000, L, 0x4163554941410000, M, 0x4262524A46420000, N, 0x1C222222221C0000, O, 0x7844784040400000, P, 0x1C222222221C0200, Q, 0x7844785048440000, R, 0x1C22100C221C0000, S, 0x7F08080808080000, T, 0x42424242423C0000, U, 0x8142422424180000, V, 0x4141495563410000, W, 0x4224181824420000, X, 0x4122140808080000, Y, 0x7E040810207E0000, Z".split(", ")
chars = [v[2:] for i,v in enumerate(chars) if i%2==0]

# Get inputs word.
a_word = input()

# Store the reprsentation for each character in input, in array.
out = []
for char in a_word:
    out += [[]]
    val = chars[ord(char)-ord("A")]
    for i in range(0,16,2):
        h = bin(int(val[i:i+2],16))[2:].zfill(8)
        out[-1].append([h.replace("0"," ").replace("1","X")])

# Print each line, remove and trailing spaces.
for i in range(len(out[0])):
    row = []
    for j in range(len(out)):
        row += ["".join(out[j][i])] if j != 0 else [""+"".join(out[j][i])]
    row = "".join(row)
    if row != " "*len(row):
        print(row.rstrip())
