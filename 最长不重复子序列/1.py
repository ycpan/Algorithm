def solve(s):
    # write your code here
    res = 0
    if s is None or len(s) == 0:
        return res
    d = {}
    tmp = 0
    start = 0
    for i in range(len(s)):
        if s[i] in d and d[s[i]] >= start:
            start = d[s[i]] + 1
        tmp = i - start + 1
        d[s[i]] = i
        res = max(res, tmp)
    return res
if __name__ == '__main__':
    s = 'abcabcbb'
    print(solve(s))
    s = 'bbbbb'
    print(solve(s))
    s = 'pwwkees'
    print(solve(s))
    s = ''
    print(solve(s))
