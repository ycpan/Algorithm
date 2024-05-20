# 返回最少硬币的个数
def coinChange(coins, amount):
    # 初始化动态规划数组
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    import ipdb
    ipdb.set_trace()
    # 更新dp数组
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    # 如果dp[amount]仍然是初始时设置的一个很大的数，返回-1
    return dp[amount] if dp[amount] != float('inf') else -1
# 测试示例
print(coinChange([1, 2, 5], 11))  # 输出应该是 3
print(coinChange([2], 3))         # 输出应该是 -1
print(coinChange([1], 0))         # 输出应该是 0
