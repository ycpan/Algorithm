def longest_valid_parentheses(s: str) -> int:
    stack = [-1]
    max_length = 0
    import ipdb
    ipdb.set_trace()
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    if stack:
        max_length = max(max_length, len(s) - 1 - stack[-1])
    return max_length
# 测试示例
test_cases = ["(()", ")()())", ""]
results = [longest_valid_parentheses(tc) for tc in test_cases]
