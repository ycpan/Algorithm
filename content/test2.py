def permute(nums):
    def backtrack(start, end):
        import ipdb
        ipdb.set_trace()
        if start == end:
            import ipdb
            ipdb.set_trace()
            output.append(nums[:])
        for i in range(start, end):
            # 交换当前索引和起始索引的数字
            nums[start], nums[i] = nums[i], nums[start]
            # 递归调用，起始索引向后移动一位
            backtrack(start + 1, end)
            # 回溯，交换回来
            nums[start], nums[i] = nums[i], nums[start]

    output = []
    backtrack(0, len(nums))
    return output
# 示例
nums = [1,2,3]
print(permute(nums))
