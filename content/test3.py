def combinationSum(candidates, target):
    def backtrack(start, target, path):
        import ipdb
        ipdb.set_trace()
        # 如果当前和等于目标数，说明找到一个组合
        if target == 0:
            output.append(path[:])
            return
        # 如果当前和小于目标数，继续寻找下一个数字
        for i in range(start, len(candidates)):
            # 如果当前数字大于目标数，则无需继续
            if candidates[i] > target:
                break
            # 选择当前数字，加入到路径中
            path.append(candidates[i])
            # 递归调用，处理剩余的目标数
            backtrack(i, target - candidates[i], path)
            # 回溯，撤销选择
            path.pop()

    output = []
    backtrack(0, target, [])
    return output
# 示例
candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))
