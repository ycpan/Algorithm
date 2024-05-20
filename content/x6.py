def numSquares(n):
    # 初始化动态规划数组
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    # 计算完全平方数
    i = 1
    while i * i <= n:
        square = i * i
        # 更新dp数组
        import ipdb
        ipdb.set_trace()
        for j in range(square, n + 1):
            dp[j] = min(dp[j], dp[j - square] + 1)
        i += 1
    return dp[n]
# 测试示例
print(numSquares(12))  # 输出应该是 3
print(numSquares(13))  # 输出应该是 2
