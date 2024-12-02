# Get inputs.
n = int(input())
for _ in range(n):
    x = input()
    start_value = x
    
    # Find if x is happy or not.
    seen = set()
    while x not in seen and int(x) != 1:
        seen.add(x)
        val = 0
        for i in x:
            val += int(i)**2
        x = str(val)

    # Print correct face depending on if x is happy or not.
    if x in seen or x == "-1":
        print(f"{start_value} :(")
    else:
        print(f"{start_value} :)")
