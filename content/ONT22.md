# 最长不含重复字符的子字符串
## 问题
**描述**  
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
数据范围:  
**示例1：**
```
输入：
"abcabcbb"
返回值：
3
说明：
因为无重复字符的最长子串是"abc"，所以其长度为 3。
```
**示例2：**
```
输入：
"pwwkew"
返回值：
3
说明：
因为无重复字符的最长子串是 "wke"，所以其长度为 3。
请注意，你的答案必须是子串的长度，"pwke" 是一个子序列，不是子串。
```
## 问题分析
- **子串：** 要连续
- **子序列:** 可以不连续

题目中要求是**最长不重复连续的子字符串**
## 解题
用`charIndexMap`来存储字符串对应的字符以及所在index，由于字符可能由重复，`charIndexMap`需要存储最新的index即可。然后遍历字符串，用start和end记录当前不重复连续的子字符串区间，start（默认为0），end（默认为当前字符串的位置。当前字符存在`charIndexMap`中，更新start，start + 1；如果不在，说明有可能突破包含连续子字符串的最大长度，需要更新`maxLength`  
```python
class Solution:
    def lengthOfLongestSubstring(self , s: str) -> int:
        # write code here
        if not s:
            return 0
    
        start = maxLength = 0
        charIndexMap = {}
        
        for end in range(len(s)):
            if s[end] in charIndexMap and charIndexMap[s[end]] >= start:
                start = charIndexMap[s[end]] + 1
            else:
                maxLength = max(maxLength, end - start + 1)
            
            charIndexMap[s[end]] = end
            
        return maxLength

if __name__ == '__main__':
    test1 = "abcabcbb"
    test2 = "bbbbb"
    st = Solution()
    s1 = st.lengthOfLongestSubstring(test1)
    print(s1)
    s2 = st.lengthOfLongestSubstring(test2)
    print(s2)
```
