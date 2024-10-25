# Create hashmap of elements and set required variables.
elements = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og"
elements = {char:1 for char in elements.split(" ")}
chars = []
words = set()

# Get input and create array of elements that could be used to spell that word.
word = input()
for char in word:
    if char.upper() in elements:
        chars.append(char.upper())

for i in range(len(word)-1):
    if word[i:i+2].capitalize() in elements:
        chars.append(word[i:i+2].capitalize())

# Convert to array and lowercase for better efficiency in search function.
word_lower = word.lower()
word = [i for i in word]


def search(arr):
    """
    Helper function to search through possible spelling of the word. This function implements DFS.

    Parameters:
    arr : List - List of characters in order to spell the given word.
    
    Returns - None
    """
    # Convert array to lowercase string for comparision.
    word_formed = "".join(arr).lower()
    size = len(arr)

    # If length of array is larger than given word or current doesn't equal given word - Return
    if size > len(word) or word_formed[0:size] != word_lower[0:size]:
        return False
    
    # Goal case - Word has been formed so add to set. Set is used for unique spellings only.
    if word_formed == word_lower:
        words.add("".join(arr))
        return True

    # DFS element - Search all possible combinations.
    for i in range(0, len(chars)):
        tmp = [i for i in arr]
        for j in range(len(chars[i])):
            tmp += chars[i][j]
        search(tmp)

# Call DFS function.
search([])

# Return ordered words, one per line. none if no words have been formed.
words = sorted(list(words))
if words:
    print(*[i for i in words],sep="\n")
else:
    print("none")
