def min_jumps(nums):
    n = len(nums)
    if n <= 1:
        return 0
    jumps = 0
    currentFarthest = 0
    nextFarthest = 0
    for i in range(n - 1):
        if i == 2:
            import ipdb
            ipdb.set_trace()
        nextFarthest = max(nextFarthest, i + nums[i])
        if i == currentFarthest:
            jumps += 1
            currentFarthest = nextFarthest
    return jumps
# 测试示例
example1 = [2, 3, 1, 1, 4]
example2 = [2, 3, 0, 1, 4]
#xy=min_jumps(example1)
#print(xy)
#xy1=min_jumps(example2)
#print(xy1)
## 这个应该跳不出来，测试
example2 = [2, 1, 0, 1, 4]
xy=min_jumps(example2)
