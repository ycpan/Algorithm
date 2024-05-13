def generateParenthesis(n):
    def backtrack(S='', left=0, right=0):
        import ipdb
        ipdb.set_trace()
        if len(S) == 2 * n:
            ans.append(S)
            return
        if left < n:
            backtrack(S + '(', left + 1, right)
        if right < left:
            backtrack(S + ')', left, right + 1)
    ans = []
    backtrack()
    return ans
# 示例
n = 3
print(generateParenthesis(n))
