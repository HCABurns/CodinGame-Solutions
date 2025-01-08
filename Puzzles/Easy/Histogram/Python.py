# Import for custom round
import math

def custom_round(n):
    """
    Custom round to ensure 0.5 rounds up.

    Parameter:
    n : float - Float to be rounded.

    Returns: int - Float rounded to correct integer.
    """
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    else:
        return math.ceil(n)

# Get inputs.
s = input().upper()

# Find the frequencies and convert to percentage for all alphabetical characters.
chars = {i:s.count(i) for i in s if i.isalpha()}
chars_count = sum([v for v in chars.values()])
chars = {i:round(float(v)/chars_count*100,2) for i,v in chars.items()}

# Print out the histogram. (Custom round as python uses bankers rounding causing wrong answer)
for i in range(0,26):
    char = chr(ord("A")+i)
    size = custom_round(chars.get(char,0))
    if i == 0:print("  +"+ "-"*size + ["+" if size > 0 else ""][0])
    print(char+ " " + ["","|"][size != 0] + " "*size + f"|{chars.get(char,0):.2f}%")
    
    m = custom_round(chars.get(char,0))
    n = custom_round(chars.get(chr(ord(char)+1),0))

    size = custom_round(max(chars.get(char,0), chars.get(chr(ord(char)+1),0)))
    f = [i for i in "  +"+ "-"*size + ["+" if size > 0 else ""][0]]
    
    if m != 0: f[m+3] = "+"
    if n != 0: f[n+3] = "+"

    print("".join(f))
