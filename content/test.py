from collections import defaultdict
def subarray_sum(nums, k):
    # 初始化哈希表和前缀和
    count = defaultdict(int)
    import ipdb
    ipdb.set_trace()
    count[0] = 1  # 初始化前缀和为0的出现次数为1
    prefix_sum = 0
    result = 0
    # 遍历数组
    for num in nums:
        # 计算前缀和
        prefix_sum += num
        # 如果存在前缀和为 prefix_sum - k 的记录，则说明存在一个子数组的和为 k
        if prefix_sum - k in count:
            result += count[prefix_sum - k]
        # 在哈希表中记录前缀和的出现次数
        count[prefix_sum] += 1
    return result
# 示例数组
nums1 = [1, 1, 1]
k1 = 2
nums2 = [1, 2, 3]
k2 = 3
# 计算和为 k 的子数组的个数
subarray_sum(nums1, k1), subarray_sum(nums2, k2)
(2, 2)
