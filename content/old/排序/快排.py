#def quick_sort(li):
#    low = 0
#    high = len(li) - 1
#    pivot = li[(low + high) // 2]
#    while(low < high):
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == '__main__':
    # 测试快速排序函数
    arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)



    #li = [3,1,5,2,7,0,9]
    #s_li = quick_sort(li)
    #print(s_li)
