def longest_common_subsequence_indexes(X, Y):
    m = len(X)
    n = len(Y)
    # 创建一个二维数组来存储动态规划表
    dp = [[0] * (n+1) for _ in range(m+1)]
    # 填充动态规划表
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # 回溯以找到最长公共子序列
    i = m
    j = n
    lcs = []
    lcs_indexes = []
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs.append(X[i-1])
            lcs_indexes.append((i-1, j-1))  # 记录索引
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    # 由于我们是从后往前构建子序列的，所以需要将其反转
    lcs = lcs[::-1]
    lcs_indexes = lcs_indexes[::-1]
    return lcs, lcs_indexes
# 测试代码
X = "ABCBDAB"
Y = "BDCAB"
lcs, lcs_indexes = longest_common_subsequence_indexes(X, Y)
print("最长公共子序列:", lcs)
print("对应索引:", lcs_indexes)

