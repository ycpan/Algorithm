def trap(height):
    # 初始化左右指针和最大雨水量
    left, right = 0, len(height) - 1
    max_water = 0
    left_max = right_max = 0
    # 当左指针小于右指针时继续
    while left < right:
        # 更新左右柱子的最大高度
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])
        # 如果左边的柱子较矮
        import ipdb
        ipdb.set_trace()
        if height[left] < height[right]:
            # 计算当前雨水量，并加到最大雨水量中
            max_water += left_max - height[left]
            # 移动左指针
            left += 1
        else:
            # 计算当前雨水量，并加到最大雨水量中
            max_water += right_max - height[right]
            # 移动右指针
            right -= 1
    return max_water
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res = trap(height1)
print(res)
