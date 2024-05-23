def quick_sort(li):
    quick_sort1(li, 0, len(li) - 1)
    return li

def quick_sort1(li, start, end):
    if start < end:
        pivot = partion(li, start, end)
        quick_sort1(li, start, pivot - 1)
        quick_sort1(li, pivot + 1, end)

def partion(li, low, high):
    pivot = li[low]
    while low < high:
        while low < high and li[high] >= pivot:
            high -= 1
        li[low] = li[high]
        while low < high and li[low] <= pivot:
            low += 1
        li[high] = li[low]
    li[low] = pivot
    return low

li = [3, 8, 2, 5, 1]
sorted_li = quick_sort(li)
print(sorted_li)

