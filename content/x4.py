# 杨辉三角
def generate(numRows):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    result = [[1]]
    for i in range(1, numRows):
        prev_row = result[-1]
        new_row = [1]  # 每一行开始都是 1
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # 每一行结束也是 1
        result.append(new_row)
    return result
# 测试示例
example1 = generate(5)
example2 = generate(1)
example1, example2
([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], [[1]])
