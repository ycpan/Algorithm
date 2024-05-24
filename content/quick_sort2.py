def solve(li):
    def swap(i,j):
        li[i],li[j] = li[j],li[i]
    def quick_sort(start,end):
        original_start = start
        pivot = li[original_start]
        #import ipdb
        #ipdb.set_trace()
        while start < end:
            while start < end and li[end] >= pivot:
                end -= 1
            while start < end and li[start] <= pivot:
                start += 1
            if start < end:
                swap(start,end)
        #li[start] = pivot
        swap(original_start,start)
        #if start == k:
        #    return li[start]
        #if start <
        return start
    def my_quick_sort(start,end):
        if start < end:
            pivot_index = quick_sort(start,end)
            my_quick_sort(start,pivot_index - 1)
            my_quick_sort(pivot_index + 1,end)
    my_quick_sort(0,len(li)-1)
    return li
li = [3,2,8,9,1]
new_li = solve(li)
print(new_li)

