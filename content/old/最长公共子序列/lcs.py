# 计算两个字符串的最长公共子序列（Longest Common Subsequence, LCS）的长度
def longestCommonSubsequence(text1, text2):
    # calculate the size of the first and second string
    sz1, sz2 = len(text1), len(text2)
    #tmp, dp = [0]*(sz2+1), [0]*(sz2+1)：创建两个列表 tmp 和 dp，它们的长度分别是 sz2 + 1。列表 dp 用于存储动态规划的结果，而 tmp 用于存储中间结果。
    tmp, dp = [0]*(sz2+1), [0]*(sz2+1)
    for i in range(0, sz1):
        for j in range(0,  sz2):
            # tmp[j+1] = dp[j] + \    1 if text1[i] == text2[j] else max(tmp[j], dp[j+1])：这一行使用了条件表达式来更新 tmp 列表。如果当前字符 text1[i] 和 text2[j] 相等，那么 tmp[j+1] 就是 dp[j] + 1，表示当前字符与前一个字符（如果有的话）一起构成了一个更长的公共子序列。如果不相等，那么 tmp[j+1] 就是 max(tmp[j], dp[j+1])，即当前字符与下一个字符（如果有的话）构成的公共子序列的最大长度。
            tmp[j+1] = dp[j] + \
                1 if text1[i] == text2[j] else max(tmp[j], dp[j+1])
        tmp, dp = dp, tmp
    return dp[-1]
if __name__ == '__main__':
    lcs = longestCommonSubsequence('dfadb','dfb')
    print(lcs)
