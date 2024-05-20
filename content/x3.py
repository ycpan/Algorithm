def climb_stairs(n):
    if n <= 2:
        return n
    # 初始化前两个值
    a, b = 1, 2
    # 迭代求解
    for _ in range(2, n):
        a, b = b, a + b
    return b
# 测试示例
example1 = climb_stairs(2)  # 应该返回 2
example2 = climb_stairs(3)  # 应该返回 3
example1, example2
(2, 3)
