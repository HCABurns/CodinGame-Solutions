# Hashmap for conversion.
MORSE = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..'}

# Get the unknown morse and store length.
unknown_morse = input()
unknown_morse_length = len(unknown_morse)

# Convert words into morse.
words_keys = ["".join(map(lambda char:MORSE[char] , [char for char in input()])) for i in range(int(input()))]

# Create a cache for memoization.
cache = {unknown_morse_length:1}
def search(idx):
    # If idx is length of morse, it's a valid combination.
    if idx == unknown_morse_length:
        return 1

    # If idx in cache then return result.
    if idx in cache:
        return cache[idx]

    # Recursively search if current combination is equal to the unknown_morse of the same length.
    combinations = 0
    for word in words_keys:
        if unknown_morse[idx:idx+len(word)] == word:
            combinations += search(idx+len(word))
    # Cache result and return.
    cache[idx] = combinations
    return combinations

# Return the number of possible ways to dorm unknown morse with given dictionary.
print(search(0))
