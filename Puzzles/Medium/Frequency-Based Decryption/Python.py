# Get input, create variable with only letters and store size.
message = input()
chars_only = "".join(i for i in message if i.isalpha())
m_length = len(chars_only)

# Set characters and frequencies, order based on frequency. Get string of letters in order of frequency.
expected_frequencies = sorted({"A": 8.08, "B": 1.67, "C": 3.18, "D": 3.99, "E": 12.56,"F": 2.17, "G": 1.80, "H": 5.27, "I": 7.24, "J": 0.14,"K": 0.63, "L": 4.04, "M": 2.60, "N": 7.38, "O": 7.47,"P": 1.91, "Q": 0.09, "R": 6.42, "S": 6.59, "T": 9.15,"U": 2.79, "V": 1.00, "W": 1.89, "X": 0.21, "Y": 1.65, "Z": 0.07}.items() , key = lambda x : x[1] , reverse=True)
order = "".join([i[0] for i in expected_frequencies])[::-1]

def shifter(message , shift_amount):
    """
    Helper function to shift message by X amount.

    Parameters:
    message : string - String to be shifted.
    shift_amount : int - Amount to be shifted.

    Return : string - Shifted string.
    """
    shifted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                char = chr(ord("A") + (ord(char)+shift_amount-ord("A"))%26)
            else:
                char = chr(ord("a") + (ord(char)+shift_amount-ord("a"))%26)
        shifted_message += char
    return shifted_message

# Shift and compare frequencies of shifted to expected. Count total and pick shift that has the most matches.
# For equal matches, select match with first shift being a larger frequency.
best_match = []
for shift in range(26):
    shifted = shifter(message , shift)
    # Order by frequency, if two are equal, order of precedence is based on position in expected.
    shifted_frequencies = sorted({char.upper():(shifted.count(char.lower())+shifted.count(char.upper()))/m_length/0.01 for char in [c for c in shifted if c.isalpha()]}.items(), key = lambda x : (x[1],order.index(x[0])) , reverse = True)
    count = []
    for j,k in zip(expected_frequencies[:6] , shifted_frequencies[:6]):
        if j[0] == k[0]:
            count += [1]
        else:
            count += [0]
    best_match = max(best_match , [count , shifted])
print(best_match[1])
