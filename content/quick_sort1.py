def quick_sort(li):
    def partion(start,end):
        pivot = li[start]
        while(start < end):
            while start < end and li[end] >= pivot:
                end -= 1
            li[start]=li[end]
            while start < end and li[start] <= pivot:
                start += 1
            li[end] = li[start]
        li[start] = pivot
        return start
    def sub_quick_sort(start,end):
        if start < end:
            pivot_index = partion(start,end)
            sub_quick_sort(start,pivot_index - 1)
            sub_quick_sort(pivot_index + 1,end)
    sub_quick_sort(0,len(li)-1)
    return li
if __name__ == '__main__':
    li = [3,2,8,9,1]
    new_li = quick_sort(li)
    print(li)

