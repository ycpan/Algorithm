def letterCombinations(digits):
    if not digits:
        return []
    # 创建数字到字母的映射
    phone = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def backtrack(index, path):
        # 如果路径长度等于数字长度，说明一个组合完成
        import ipdb
        ipdb.set_trace()
        if len(path) == len(digits):
            output.append(''.join(path))
            return
        # 获取当前数字对应的字母
        for letter in phone[digits[index]]:
            # 选择当前字母，加入到路径中
            path.append(letter)
            # 递归调用，处理下一个数字
            backtrack(index + 1, path)
            # 回溯，撤销选择
            path.pop()

    output = []
    backtrack(0, [])
    return output
# 示例
digits = "23"
print(letterCombinations(digits))
