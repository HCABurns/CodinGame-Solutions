# Create hashmap for special characters, and set for numbers.
special_character_hashmap = {"sp":" ", "bS":"\\", "sQ":"'", "nl":"\n"}
numbers_set = {"1","2","3","4","5","6","7","8","9","0"}

for i in input().split(" "):
    # Check if newline character - If found print newline and continue (Move on to next item from input)
    if i == "nl":
        print("")
        continue

    # Check if all numbers in input. If so then output.
    if all([1 if j in numbers_set else 0 for j in i]):
        print(i[-1]*int(i[:-1]),end="")

    # Split the input into numbers and characters.
    quantity = int("".join([j for j in i if j in numbers_set]))
    string = "".join([j for j in i if j not in numbers_set])

    # Print correct char * quantity (Replace special characters with char in hashmap)
    o=""
    if string in special_character_hashmap:
        o=special_character_hashmap[string]*quantity
    else:
        o=string*quantity
    print(o,end="")
