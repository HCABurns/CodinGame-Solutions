# Get answer and form set.
answer = input()
answer_set = set(answer)
n = int(input())
for _ in range(n):
    # Get attempt and form hashmap.
    word = input()
    attempt = {j: answer.count(j) for j in word}
    
    # Set correct positions.
    out = ["X" for _ in range(len(answer))]
    for i in range(len(out)):
        if word[i] == answer[i]:
            out[i] = "#"
            attempt[word[i]] -= 1
    
    # Find any out of position letters.
    for i,char in enumerate(word):
        count = attempt[word[i]]
        if char in answer_set and count > 0 and out[i] != "#":
            out[i] = "O"
            attempt[char] -= 1

    # Output result of guess.
    print("".join(out))
