# Hashmap to convert to roman numerals.
translator = {
1:"I",
4:"IV",
5:"V",
9:"IX",
10:"X",
40:"XL",
50:"L",
90:"XC",
100:"C",
400:"CD",
500:"D",
900:"CM",
1000:"M"}
values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

def to_roman(value):
    """
    Function to convert decimal to roman numerals.

    Parameter:
    value : int - Decimal value to be converted.

    Return : string - Roman numeral representation of the given value.
    """
    roman = ""
    i = 0
    while value != 0:
        if value - values[i] >= 0:
            roman+=translator[values[i]]
            value -= values[i]
        else:
            i+=1
    return roman

# Convert numbers to roman numerals and store as tuple with given number.
numbers = []
n = int(input())
for i in range(n):
    x = int(input())
    numbers.append((to_roman(x),x))

# Sort and print in increasing alphabetical order.
numbers.sort(key = lambda x:x[0])
print(*[number[1] for number in numbers])
