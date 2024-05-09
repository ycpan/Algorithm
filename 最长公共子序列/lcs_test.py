def commonOfLongestSubsequence(s1,s2):
    s1_len,s2_len = len(s1),len(s2)
    tmp,dp = [0]*(s2_len + 1),[0]*(s2_len + 1)
    for i in range(s1_len):
        for j in range(s2_len):
            #dp[j] = dp[j-1] + 1 if s1[i] == s2[j] else max(dp[j],tmp[j])
            tmp[j+1] = dp[j] + 1 if s1[i] == s2[j] else max(tmp[j],dp[j+1])
        tmp,dp = dp,tmp
    return dp[-1]
if __name__ == '__main__':
    lcs = commonOfLongestSubsequence('dfadb','dfb')
    print(lcs)
