def solve(li,k):
    def swap(i,j):
        li[i],li[j] = li[j],li[i]
    def quick_sort(start,end):
        original_start = start
        pivot = li[original_start]
        while start < end:
            while start < end and li[end] <= pivot: # 第k个最大的，要从大到小进行排序
                end -= 1
            while start < end and li[start] >= pivot:# 第k个最大的，要从大到小进行排序
                start += 1
            if start < end:
                swap(start,end)
        #li[start] = pivot # 上文用到了交换，而不是一个接着一个的赋值，所以这里也带用交换，否则最新start位置上的元素会被覆盖掉。
        swap(original_start,start)
        #if start == k:
        #    return li[start]
        #if start <

        return start
    def my_quick_sort(start,end):
        res = None
        if start < end:
            pivot_index = quick_sort(start,end)
            #import ipdb
            #ipdb.set_trace()
            if pivot_index == k-1:
                return li[pivot_index]
            if pivot_index > k - 1:
                res = my_quick_sort(start,pivot_index - 1)
            if pivot_index < k - 1:
                res = my_quick_sort(pivot_index + 1,end)
        return res 
    res = my_quick_sort(0,len(li)-1)
    #return li
    return res
li = [3,2,8,9,1]
new_li = solve(li,3)
print(new_li)

