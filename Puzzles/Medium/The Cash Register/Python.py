# Get inputs.
register = sorted(map(int, input().split()), reverse=True)
goal_amount = int(input())

cache = {}
def min_coins(remaining_amount):
    # Base cases
    if remaining_amount == 0:
        return []
    if remaining_amount < 0:
        return None

    # Return minimum if possible.
    if remaining_amount in cache:
        return cache[remaining_amount]

    # Recursively search all combinations.
    coins = None
    for coin in register:
        result = min_coins(remaining_amount - coin)
        if result is not None and (coins is None or len(result) + 1 < len(coins)):
            coins = result + [coin]

    # Set cache.
    cache[remaining_amount] = coins
    return coins

# Print the result
result = min_coins(goal_amount)
if result is None:
    print("IMPOSSIBLE")
elif result == []:
    print(0)
else:
    print(*result[::-1])
