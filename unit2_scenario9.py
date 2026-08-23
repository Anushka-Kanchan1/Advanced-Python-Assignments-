def knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Fill the table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                # Include or exclude the item
                include = values[i - 1] + \
                          dp[i - 1][w - weights[i - 1]]

                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected items
    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i)
            w -= weights[i - 1]

    selected.reverse()

    return dp[n][capacity], selected


# Input
weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))
capacity = int(input("Enter bag capacity: "))

# Calculate result
maximum_value, items = knapsack(weights, values, capacity)

# Output
print("\nMaximum Value:", maximum_value)
print("Selected Items:", items)
print("Total Weight:",
      sum(weights[i - 1] for i in items))


OUTPUT 

Enter weights: 2 3 4 5
Enter values: 3 4 5 6
Enter bag capacity: 5

Maximum Value: 7
Selected Items: [1, 2]
Total Weight: 5
