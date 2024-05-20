def lengthOfLIS(nums):
    if not nums:
        return 0
    # 初始化dp数组
    dp = [1] * len(nums)
    # 遍历数组nums
    for i in range(len(nums)):
        import ipdb
        ipdb.set_trace()
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    # 返回dp数组中的最大值
    return max(dp)
# 测试示例
print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 输出应该是 4
print(lengthOfLIS([0, 1, 0, 3, 2, 3]))           # 输出应该是 4
print(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))        # 输出应该是 1
