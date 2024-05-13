def combinationSum(candidates, target):
    def backtrack(remaining, comb, start):
        import ipdb
        ipdb.set_trace()
        if remaining == 0:
            result.append(list(comb))
            return
        elif remaining < 0:
            # 超过了目标，所以不需要继续递归
            return
        for i in range(start, len(candidates)):
            # 选择当前数字，加入到组合中
            comb.append(candidates[i])
            # 给剩余的目标减去当前数字，并递归
            backtrack(remaining - candidates[i], comb, i)
            # 撤销选择，以便尝试其他数字
            comb.pop()
    result = []
    backtrack(target, [], 0)
    return result
# 示例 1
print(combinationSum([2,3,6,7], 7))  # 输出：[[2,2,3],[7]]
# 示例 2
print(combinationSum([2,3,5], 8))  # 输出：[[2,2,2,2],[2,3,3],[3,5]]
# 示例 3
print(combinationSum([2], 1))  # 输出：[]
