def next_permutation(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Step 1: Find the first index i such that nums[i] < nums[i+1]
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    # If no such index found, then the permutation is the smallest,
    # so we just reverse the list
    if i == -1:
        nums.reverse()
        return
    # Step 2: Find the first index j such that nums[j] > nums[i]
    j = len(nums) - 1
    while j >= 0 and nums[j] <= nums[i]:
        j -= 1
    # Step 3: Swap nums[i] and nums[j]
    nums[i], nums[j] = nums[j], nums[i]
    # Step 4: Reverse the sublist nums[i+1:]
    nums[i + 1:] = reversed(nums[i + 1:])
# 测试示例
test_cases = [[1,2,3], [3,2,1], [1,1,5]]
for nums in test_cases:
    next_permutation(nums)
    print(nums)
