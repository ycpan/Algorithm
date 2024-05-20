def wordBreak(s, wordDict):
    # 初始化动态规划数组
    dp = [False] * (len(s) + 1)
    dp[0] = True
    # 遍历字符串s的所有子串
    for i in range(1, len(s) + 1):
        for j in range(i):
            import ipdb
            ipdb.set_trace()
            # 如果dp[j]为True且s[j:i]在字典中，则更新dp[i]
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[len(s)]
# 测试示例
print(wordBreak("leetcode", ["leet", "code"]))  # 输出应该是 True
print(wordBreak("applepenapple", ["apple", "pen"]))  # 输出应该是 True
print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # 输出应该是 False
