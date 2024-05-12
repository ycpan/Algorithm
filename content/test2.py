def minWindow(s, t):
    from collections import Counter
    
    # 初始化 need 和 window 计数器
    need = Counter(t)
    window = {}
    
    # 初始化左右指针
    left = right = 0
    
    # 表示窗口中满足 need 条件的字符个数
    valid = 0
    
    # 记录最小覆盖子串的起始位置和长度
    start, length = 0, float('inf')
    
    while right < len(s):
        # c 是将移入窗口的字符
        c = s[right]
        # 右移窗口
        right += 1
        
        # 进行窗口内数据的一系列更新
        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1
        
        # 判断左侧窗口是否要收缩
        while valid == len(need):
            # 更新最小覆盖子串
            if right - left < length:#这个条件判定是必要的，当达到这一步的时候，说明right已经固定下来了，右移left，不断缩小长度，只有在length大于right-left的时候，说明left移动的还没有超过理想值；当length小于等于left的时候，
                start = left
                length = right - left
            else:
                import ipdb
                ipdb.set_trace()
                print(left)
            
            # d 是将移出窗口的字符
            d = s[left]
            # 左移窗口
            left += 1
            
            # 进行窗口内数据的一系列更新
            if d in need:#如果d not in need，valid保持不变，while valid == len(need)就会一直有效，left就会一直右移。
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1 # windows[d] >= need[d]的，当windows[d] > need[d]的时候，只更新window[d]
    
    # 返回最小覆盖子串
    return "" if length == float('inf') else s[start:start + length]
# 示例
s = "cabwefgewcwaefgcf"
t = "cae"
print(minWindow(s, t))  # 输出: "cwae"
