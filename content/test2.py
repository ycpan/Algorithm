def findKthLargest(nums, k):
    # 交换位置i和位置j的元素
    def swap(i: int, j: int):
        nums[i], nums[j] = nums[j], nums[i]

    # 对[left, right]范围内的元素进行降序快排，找到第k大元素
    def quick_sort_kth_element(k: int, left: int, right: int) -> int:
        mid = (right + left) // 2    # 选取中间元素作为切分值
        swap(mid, right)             # 将切分值放到右边界避免加入元素的划分
        partition, i, j = nums[right], left, right   # 双指针从左右边界开始，分别找到要交换的元素
        while i < j:
            while i < j and nums[i] >= partition: i += 1    # 找到左侧小于切分值的元素
            while j > i and nums[j] <= partition: j -=1    # 找到右侧大于切分值的元素【因为是找大于，即使j从right开始，right也不会被选中】
            if i < j:
                swap(i, j)     # 将大于元素放到左侧，小于元素放到右侧
        swap(i, right)     # i最后停留的位置一定是右侧首个小于切分值的元素，与切分值交换，则[left, i)都是大于（等于）切分值，[i+1, right]都是小于（等于）切分值
        if i == k - 1: return nums[i]   # 如果切分值就是第k大元素，直接返回
        if i < k - 1: return quick_sort_kth_element(k, i + 1, right)     # 切分值是第k大之前的元素，在右区间搜索第k大
        return quick_sort_kth_element(k, left, i - 1)   # 切分值是第k大之后的元素，在左区间搜索第k大
    
    return quick_sort_kth_element(k, 0, len(nums) - 1)    # 快排整个区间
# 测试示例
test_cases = [
    ([3, 2, 1, 5, 6, 4], 2),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
]
results = [findKthLargest(tc[0], tc[1]) for tc in test_cases]
print(results)

