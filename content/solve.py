def solve(n):
    dp= [float('inf')] * (n + 1)
    dp[0] = 0

    import ipdb
    ipdb.set_trace()
    for i in range(n):
        square = i*i
        for j in range(square,n+1):
            dp[j] = min(dp[j],dp[j - square] + 1)

    return dp[n]
print(solve(12))  # 输出应该是 3
