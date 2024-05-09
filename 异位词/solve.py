#leetcode 49
#给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
#
#字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
#
#
#
#示例 1:
#
#输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
#示例 2:
#
#输入: strs = [""]
#输出: [[""]]

def groupAnagrams(strs):
    anagrams = {}
    for s in strs:
        # 计算每个字符串的频率字典
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        # 将频率字典作为键，字符串列表作为值添加到哈希表中
        # freq = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        if tuple(freq) in anagrams:
            anagrams[tuple(freq)].append(s)
        else:
            anagrams[tuple(freq)] = [s]
            # anagrams = {(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat']}
    return list(anagrams.values())

# 测试给定的示例
test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
test2 = [""]

print(groupAnagrams(test1)),print(groupAnagrams(test2))

