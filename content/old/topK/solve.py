def quick_sort(nums, k):
    # 从nums数组中选择最大的k个数，并且不使用额外存储空间
    # 这个时间复杂度为nlogn,时间复杂度并不是最优的
    # 最优的是从数组num中随机选一个数字，如果比这个数字大，就放在一堆A中，如果小，就放在另一堆B中；如果堆A中的元素大于k个，从堆A中选k个；如果小于k个，则从堆B中选k-len(堆A)个数字.时间复杂度平均为n
    
    start = 0
    end = len(nums) - 1
    if k > len(nums):
        return 
    def quick_sort_1(start,end,nums):
        i = start
        j = end
        if i >= j:
            return
        flag = data[start]
        while i < j:
            while i<j and data[j] >= flag:
                j -= 1
            data[i] = data[j]
            while i < j and data[i] <= flag:
                i += 1
            data[j] = data[i]
        data[i] = flag
        quickSort(data,start,i - 1)
        quickSort(data,i + 1,end)
    quick_sort_1(start,end,nums)
    return nums[end-k:]
