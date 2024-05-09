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
