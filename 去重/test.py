#问题1：numpy self attention
#问题2：蒙特卡洛
#问题3：有一个有序数组，需要删除重复出现的元素，定义出现次数超过两次的元素为重复出现的元素，要求返回删除之后的数组的新长度。
#不要使用额外的数组空间，在 原地 修改输入数组，并在使用 O(1) 额外空间的条件下完成。
#1. 输入：nums = [1,1,1,2,2,3]
#   输出：5, nums = [1,1,2,2,3]
#   解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。
#
#2. 输入：nums = [0,0,1,1,1,1,2,3,3]
#   输出：7, nums = [0,0,1,1,2,3,3]
#   解释：函数应返回新长度 length = 7, 并且原数组的前七个元素被修改为 0, 0, 1, 1, 2, 3, 3 。 不需要考虑数组中超出新长度后面的元素。
# [0,0,1,1,1,1,2,3,3] [0,0,1,1,1,1,2,3,3]
#li = [0,0,1,1,1,1,2,3,3]
# 要点，有序，空间复杂度为o(1),空间复杂度为o(1)并不是说只要求一个变量。
def solve(li):
    new_array_i = 0
    for i in range(len(li)):
        if i < 2:
            new_array_i = i
            continue
        if li[new_array_i] == li[i]:
            if  li[new_array_i] == li[new_array_i - 1]:
                pass
            else:
                new_array_i += 1
                li[new_array_i] = li[i]
        else:
            new_array_i += 1
            li[new_array_i] = li[i]
    return li[0:new_array_i + 1]
if __name__ == '__main__':
    li = [1,1,1,2,2,3]
    s_li = solve(li)
    print(s_li)
    print('expectation:{}'.format([1,1,2,2,3]))
    li = [0,0,1,1,1,1,2,3,3]
    s_li = solve(li)
    print(s_li)
    print('expectation:{}'.format([0,0,1,1,2,3,3]))
