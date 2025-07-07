from collections import defaultdict

s = input()
k = int(input())
chars = set()
max_length = current_length = idx = 0
char_counts = defaultdict(int)

for i in range(len(s)):
    if len(chars) == k and s[i] not in chars:
        while len(chars) == k:
            current_length -= 1
            char_counts[s[idx]] -= 1
            if char_counts[s[idx]] == 0:
                chars.remove(s[idx])
            idx += 1
    chars.add(s[i])
    char_counts[s[i]] += 1  
    current_length += 1
    max_length = max(max_length, current_length)
print(max_length)
