#https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=295&tqId=23255&ru=/exam/company&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Fcompany
#大家都知道斐波那契数列，现在要求输入一个正整数n,请你输出斐波那契数列的第 n 项。
#斐波那契数列是一个满足$\begin{array}{c} fib(x)=\left\{ \begin{array}{rcl} 1 & {x=1,2}\\ fib(x-1)+fib(x-2)  &{x>2}\\ \end{array} \right. \end{array}$
#数据据范围$1\leq n\leq 40$
#示例1
#输入：
#4
#返回值：
#3
#说明：
#根据斐波那契数列的定义可知，fib(1)=1,fib(2)=1,fib(3)=fib(3-1)+fib(3-2)=2,fib(4)=fib(4-1)+fib(4-2)=3，所以答案为3。   
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        #斐波拉契数的边界条件： F(0)=0 和 F(1)=1
        if n < 2:
            return n
        else:
            a, b = 0, 1
            for i in range(n-1):
                a, b = b, a + b        #状态转移方程，每次滚动更新数组

            return b
if __name__ == '__main__':
    st = Solution()
    s = st.Fibonacci(4)
    print(s)
#时间复杂度：O(n) (根据状态转移方程和边界条件，可以得到时间复杂度 O(n))
#空间复杂度：O(n) (同上)
