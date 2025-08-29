# Get input.
s = []
n = int(input())
for i in range(n):
    cgxline = input()
    s.append(cgxline)
s = "".join(s)

# Perform formatter.
tabs = 0
valid = False
i = 0
in_quotes = 0
while i < len(s):
    
    char = s[i]
    if not valid and char == " " or char == "\t":
        i+=1
        continue
    else:
        valid = True

    if char == "(":
        print("    "*tabs + "(")
        tabs += 1
        valid = False
        i+=1

    elif char == ")":
        tabs-=1
        if i+1 < len(s) and s[i+1] == ";":
            print("    "*tabs + ");")
            i+=1
        else:
            print("    "*tabs + ")")
        valid = False
        i+=1
    else:
        text = ["    "*tabs] if tabs > 0 else []
        equals = False
        while i < len(s):

            if i < len(s) and s[i] == "'":
                in_quotes = 1^in_quotes

            if equals and (s[i] == "\t" or s[i] == " "):
                i+=1
                continue
            else:
                equals = False
            
            if s[i] == "=" and not in_quotes:
                while text and text[-1] in "\t ":
                    text.pop()
                text.append("=")
                equals = True
                i+=1
                continue
            

            if (s[i] in "()" and not in_quotes):
                break
            
            text.append(s[i])
            i+=1
            if text[-1] == ";" and not in_quotes:
                break
            
        print("".join(text).rstrip())
        valid = False
