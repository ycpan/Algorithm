def solve(nums,k):
    def swap(i,j):
        nums[i],nums[j] = nums[j],nums[i]
    def quick_sort_kth_element(k,left,right):
        mid = (right + left) // 2
        swap(mid,right)
        partion,i,j = nums[right],left,right
        while i<j:
            while i<j and nums[i] >= partion:i += 1
            while j>i and nums[j] <= partion: j -= 1
            if i < j:
                swap(i,j)
        swap(i,right)
