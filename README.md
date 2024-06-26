## 解决算法的思维
动态规划，贪心算法，回溯算法
# 刷题顺序
- [ ] [求和(leetcode)](./content/1.md)

- [ ] [字母异位词分组(leetcode)](./content/49.md)

- [ ] [最长连续序列(leetcode)](./content/128.md) 
    - 不要求序列元素在原数组中连续
    - 原数组取出来后，重新排序连续即可
- [ ] [最长不含重复字符的子字符串(牛客)](./content/ONT22.md)
    - 要求原字符串连续
- [ ] [最长公共子序列(前期积累)](./content/lcs.md)
- [ ] [所有公共子序列，并返回长度和索引(前期积累)](./content/所有公共子序列.md)

- [ ] [反转链表(牛客)](./content/BM1.md)
- [ ] [二叉树最长宽度(前期积累)](./content/longest_tree_layer.md)
- [ ] [topK问题(前期积累)](./content/topK.md)
- [ ] [移动零(leetcode)](./content/283.md)
- [ ] [盛水最多的容器(leetcode)](./content/11.md)
- [ ] [三数之和(leetcode)](./content/15.md)
- [ ] [接雨水(leetcode)](./content/42.md)
    - 和盛水最多容器区别在于这个柱子可以不为0，雨水量不能相乘,盛水最多容器的话可以相乘

- [ ] [无重复字符的最长子串(leetcode)](./content/3.md)
    - 与[最长不含重复字符的子字符串(牛客)](./content/ONT22.md)一样
- [ ] [找到子符串中所有字母的异位词(leetcode)](./content/438.md)
    - 与[字母异位词分组(leetcode)](./content/49.md)的区别在于，一个是字符串，一个是数组，数组中是字符串
    - 这个是两个字符
- [ ] [和为k的子数组(leetcode)](./content/560.md)
- [ ] [滑动窗口最大值(leetcode)](./content/239.md)
- [ ] [最小覆盖子串(leetcode)](./content/76.md)     
    和[找到子符串中所有字母的异位词(leetcode)](./content/438.md)进行比较:
    - **相同点**:
        - 都是从字符串中找子串
    - **不同点**:
        - 当前的是子串里面可以有其它字符，而另一个要求不能有其它字符；这就导致，虽然两者都用到词频，但是前这是在连续的字符串上建词频，而当前的是可以在不连续的字符串上建词频。所以前者比较的是词频是否相等，当前的比较的是有效的字符数量是否相等（只有当某个字符的频率大于等于目标字符的个数时，才算一次有效）。
- [ ] [最大子数组和(leetcode)](./content/53.md)
- [ ] [合并区间(leetcode)](./content/56.md)
- [ ] [转轮数组(leetcode)](./content/189.md)
- [ ] [除自身以外数组的乘积(leetcode)](./content/238.md)
- [ ] [数组找到比左边大比右边小的元素(leetcode)](./content/找出无序数组中比左边大比右边小的元素.md)
- [ ] [缺失的第一个正数(leetcode)](./content/41.md)
    - 人家要的是最小的正数，而不是连续的最小的正数
- [ ] [矩阵置零(leetcode)](./content/73.md)
- [ ] [(螺旋矩阵(leetcode)](./content/54.md)
- [ ] [旋转图像(leetcode)](./content/48.md)
- [ ] [搜索二维矩阵(二）(leetcode)](./content/240.md)
- [ ] [相交链表(leetcode)](./content/160.md)
- [ ] [回文链表(leetcode)](./content/234.md)
- [ ] [环形链表(leetcode)](./content/141.md)
- [ ] [环形链表2(leetcode)](./content/142.md)
    - 与[环形链表(leetcode)](./content/141.md)的区别在于，这个是返回pos，那个是返回判断是否有环True或者False
- [ ] [合并两个有序链表(leetcode)](./content/21.md)
- [ ] [两数相加(leetcode)](./content/2.md)
- [ ] [删除链表的倒数第N个节点(leetcode)](./content/19.md)
- [ ] [两两交换链表中节点(leetcode)](./content/24.md)
- [ ] [k个一组反转链表(leetcode)](./content/25.md)
- [ ] [随机链表的复制(leetcode)](./content/138.md)
- [ ] [链表排序(leetcode)](./content/148.md)
- [ ] [合并K个升序链表(leetcode)](./content/23.md)
- [ ] [LRU缓存(leetcode)](./content/146.md)
- [ ] [买卖股票的最佳时机(leetcode)](./content/121.md)
- [ ] [跳跃游戏(leetcode)](./content/55.md)
- [ ] [二叉树的中序遍历(leetcode)](./content/94.md)
- [ ] [二叉树的最大深度(leetcode)](./content/104.md)
- [ ] [翻转二叉数(leetcode)](./content/226.md)
- [ ] [对称二叉树(leetcode)](./content/101.md)
- [ ] [二叉树的直径(leetcode)](./content/543.md)
- [ ] [二叉树的层序遍历(leetcode)](./content/102.md)
- [ ] [将有序的数组转换为二叉搜索树(leetcode)](./content/108.md)
- [ ] [验证二叉搜索树(leetcode)](./content/98.md)
- [ ] [二叉搜索树种地K小的元素(leetcode)](./content/230.md)
- [ ] [二叉树的右视图(leetcode)](./content/199.md)
- [ ] [从前序与中序遍历序列构造二叉树(leetcode)](./content/105.md)
- [ ] [路径总和2(leetcode)](./content/437.md)
- [ ] [二叉树的最近公共祖先(leetcode)](./content/236.md)
- [ ] [岛屿数量(leetcode)](./content/200.md)
- [ ] [跳跃游戏2(leetcode)](./content/45.md)
    - 与[跳跃游戏(leetcode)](./content/55.md)相比，这个是返回最小的跳的次数，那个是返回是否能跳
- [ ] [划分字母(leetcode)](./content/763.md)
- [ ] [腐烂的橘子(leetcode)](./content/994.md)
- [ ] [课程表(leetcode)](./content/207.md)
- [ ] [实现Trie（前缀树）(leetcode)](./content/201.md)
- [ ] [全排列(leetcode)](./content/46.md)
- [ ] [子集(leetcode)](./content/78.md)
- [ ] [电话号码的字母组合(leetcode)](./content/17.md)
- [ ] [组合总和(leetcode)](./content/39.md)
- [ ] [括号生成(leetcode)](./content/22.md)
- [ ] [单词搜索(leetcode)](./content/79.md)
- [ ] [分割回文串(leetcode)](./content/131.md)
- [ ] [N皇后(leetcode)](./content/51.md)
- [ ] [搜索插入位置(leetcode)](./content/35.md)
- [ ] [搜索二维矩阵(leetcode)](./content/74.md)
- [ ] [在排序数组中查找元素的第一个和最后一个位置(leetcode)](./content/34.md)
- [ ] [搜索旋转排序数组(leetcode)](./content/33.md)
- [ ] [寻找旋转排序数组中的最小值(leetcode)](./content/153.md)
- [ ] [寻找两个正序数组中的中位数(leetcode)](./content/4.md)
- [ ] [有效的括号(leetcode)](./content/20.md)
- [ ] [最小栈(leetcode)](./content/155.md)
- [ ] [字符串解码(leetcode)](./content/394.md)
- [ ] [每日温度(leetcode)](./content/739.md)
- [ ] [柱状图中最大矩形(leetcode)](./content/84.md)
- [ ] [数组中的第K个最大元素(leetcode)](./content/215.md)
- [ ] [前K个高频元素(leetcode)](./content/347.md)
- [ ] [数据流的中位数(leetcode)](./content/295.md)
- [ ] [爬楼梯(leetcode)](./content/70.md)
- [ ] [杨辉三角(leetcode)](./content/118.md)
- [ ] [打家劫舍(leetcode)](./content/198.md)
## 背包问题
背包问题（Knapsack problem）是一种组合优化的问题。它可以描述如下：假设有一个背包，它能承受的最大重量是 W，现在有 n 个物品，每个物品都有各自的重量 w1, w2, …, wn 和价值 v1, v2, …, vn。问如何选择装入背包的物品，使得背包中的物品总价值最大，同时不超过背包的最大承重。
背包问题有多种变体，其中最经典的是以下两种：
1. **0-1背包问题**：每种物品仅有一件，可以选择放或不放。
2. **完全背包问题**：每种物品有无限件，可以选择放任意件，包括不放。

- [ ] [完全平方数(leetcode)](./content/279.md)
- [ ] [零钱兑换(leetcode)](./content/322.md)
- [ ] [单词拆分(leetcode)](./content/139.md)
- [ ] [最长递增子序列(leetcode)](./content/300.md)
- [ ] [最长有效括号(leetcode)](./content/32.md)
- [ ] [不同路径(leetcode)](./content/62.md)
- [ ] [最小路径和(leetcode)](./content/64.md)
- [ ] [最长回文子串(leetcode)](./content/5.md)
- [ ] [最长公共子序列(leetcode)](./content/1143.md)
- [ ] [编辑距离(leetcode)](./content/72.md)
- [ ] [只出现一次数字(leetcode)](./content/136.md)
- [ ] [多数元素(leetcode)](./content/169.md)
- [ ] [下一个排列(leetcode)](./content/31.md)
- [ ] [寻找重复数(leetcode)](./content/287.md)
- [ ] [背包问题（从盒子里取糖果）(leetcode)](./content/背包问题（从盒子里取糖果）.md)
## 排序专题
- [ ] [排序专题](./content/排序.md)
