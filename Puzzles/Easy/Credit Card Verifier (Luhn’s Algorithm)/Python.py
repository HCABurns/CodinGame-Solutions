# Get number of cards to check
n = int(input())
for i in range(n):
    # Get card number,remove spaces and convert to integer.
    card = input().split(" ")
    val = "".join(card)
    val = [int(i) for i in val]

    # Step 1 and 2
    val_sum = sum([i*2 if (i*2)<10 else (i*2)-9 for i in val[::-1][1::2]])

    # Step 3
    odd_sum = sum([i for i in val[1::2]])

    #Step 4
    print("YES" if (odd_sum + val_sum) % 10 == 0 else "NO")
