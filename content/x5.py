def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    # 初始化 dp 数组
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    # 动态规划计算
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]
# 测试示例
example1 = rob([1, 2, 3, 1])  # 应该返回 4
example2 = rob([2, 7, 9, 3, 1])  # 应该返回 12
example1, example2
(4, 12)
