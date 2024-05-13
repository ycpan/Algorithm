def subsets(nums):
    def backtrack(start, path):
        import ipdb
        ipdb.set_trace()
        # 将当前路径添加到结果中
        output.append(path[:])
        # 从start开始遍历数组
        for i in range(start, len(nums)):
            # 选择当前数字，加入到路径中
            path.append(nums[i])
            # 递归调用，处理下一个数字
            backtrack(i + 1, path)
            # 回溯，撤销选择
            path.pop()

    output = []
    backtrack(0, [])
    return output
# 示例
nums = [1,2,3]
print(subsets(nums))
