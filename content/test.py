def knapsack_01(values, weights, capacity):
    """
    Solve the 0-1 Knapsack problem using dynamic programming.
    
    Parameters:
    - values: List of values for each item.
    - weights: List of weights for each item.
    - capacity: Maximum capacity of the knapsack.
    
    Returns:
    - Maximum value that can be achieved without exceeding the capacity.
    """
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    import ipdb
    ipdb.set_trace()
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Example usage
values = [6, 3, 5, 4, 6]
weights = [2, 2, 6, 5, 4]
capacity = 10
xy=knapsack_01(values, weights, capacity)
print(xy)

