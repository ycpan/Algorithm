def partition(s):
    def is_palindrome(string):
        return string == string[::-1]
    def backtrack(start, path):
        import ipdb
        ipdb.set_trace()
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start, len(s)):
            if is_palindrome(s[start:end+1]):
                path.append(s[start:end+1])
                backtrack(end+1, path)
                path.pop()
    result = []
    backtrack(0, [])
    return result
# 示例
s = "aab"
print(partition(s))  # 输出：[["a","a","b"],["aa","b"]]
