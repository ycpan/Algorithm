def solve(s):
    res = 0
    if s is None or len(s) == 0:
        return res
    d = {}
    tmp = 0
    start = 0
    # 用start来记录字符串的初始位置，d记录字符串每个字符的位置，如果有重复，则进行更新。如果该字符串在后续中出现，则更新start。然后tmp记录当前字符串与start字符串的距离。tmp和res比较，选择最大的一个。
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
