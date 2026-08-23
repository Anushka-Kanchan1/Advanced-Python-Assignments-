def coin_change(coins, amount):
    # DP table: dp[i] = number of ways to make amount i
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for value in range(coin, amount + 1):
            dp[value] += dp[value - coin]

    return dp


# Input
coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter target amount: "))

# Validation
if amount < 0 or any(c <= 0 for c in coins):
    print("Invalid input.")
else:
    dp = coin_change(coins, amount)

    print("\nNumber of ways:", dp[amount])

    print("\nDP Table:")
    for i, ways in enumerate(dp):
        print(f"Amount {i}: {ways} way(s)")

OUTPUT

Enter coin denominations: 1 2 5
Enter target amount: 5

Number of ways: 4

DP Table:
Amount 0: 1 way(s)
Amount 1: 1 way(s)
Amount 2: 2 way(s)
Amount 3: 2 way(s)
Amount 4: 3 way(s)
Amount 5: 4 way(s)
