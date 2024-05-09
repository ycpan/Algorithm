def quick_sort(li):
    if len(li) < 2:
        return li
    pivot = li[len(li) // 2]
    left = [i for i in li if i < pivot]
    middle = [i for i in li if i == pivot]
    right = [ i for i in li if i > pivot]
    return quick_sort(left) + middle + quick_sort(right)
if __name__ == '__main__':
    li = [1,9,9,2,5,7,3,0]
    s_li = quick_sort(li)
    print(s_li)
