[牛客链接](https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=295&tqId=23255&ru=/exam/company&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Fcompany)
## 问题
大家都知道斐波那契数列，现在要求输入一个正整数n,请你输出斐波那契数列的第 n 项。
斐波那契数列是一个满足$\begin{array}{c} fib(x)=\left\{ \begin{array}{rcl} 1 & {x=1,2}\\ fib(x-1)+fib(x-2)  &{x>2}\\ \end{array} \right. \end{array}$

数据据范围$1\leq n\leq 40$
```
示例1
输入：
4
返回值：
3
```
说明：
根据斐波那契数列的定义可知，fib(1)=1,fib(2)=1,fib(3)=fib(3-1)+fib(3-2)=2,fib(4)=fib(4-1)+fib(4-2)=3，所以答案为3。   
## 时间复杂为o(n)
```python
 -*- coding:utf-8 -*-
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
```
### 时间复杂度分析：
对于 n 大于等于 2 的情况，有一个从 0 到 n-2 的循环，因此时间复杂度是 O(n)。
空间复杂度分析：

该算法只使用了固定数量的变量（a, b, i），与输入规模 n 无关，因此空间复杂度是 O(1)。
综上所述，这个算法是一个时间复杂度为 O(n)，空间复杂度为 O(1) 的算法，非常高效。
## 时间复杂度为O(n)
```python
# -*- coding:utf-8 -*-

class Solution:
    def Fibonacci(self, n):
        if n < 2:
            return n

        def matrix_multiply(a, b):
            c = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        c[i][j] += a[i][k] * b[k][j]
            return c

        def matrix_power(matrix, n):
            result = [[1, 0], [0, 1]]  # 单位矩阵
            while n > 0:
                if n & 1:  # 如果n是奇数
                    result = matrix_multiply(result, matrix)
                matrix = matrix_multiply(matrix, matrix)
                n >>= 1
            return result

        matrix = [[1, 1], [1, 0]]
        result_matrix = matrix_power(matrix, n - 1)
        return result_matrix[0][0]

# 测试代码
solution = Solution()
print(solution.Fibonacci(4))  # 输出3 
```
### 时间复杂度 log(n)
### 矩阵快速幂
矩阵快速幂是一种高效计算矩阵幂的算法，它利用了分治的思想和矩阵乘法的结合律。矩阵快速幂的主要思想是将矩阵幂的运算分解成多个小的幂运算，然后通过矩阵乘法将这些小幂运算的结果合并起来。这种方法可以将时间复杂度从 O(n) 降低到 O(log n)。
以下是矩阵快速幂的基本步骤：
1. **基矩阵**：定义一个矩阵的基，对于斐波那契数列，基矩阵是 `[[1, 1], [1, 0]]`。
2. **矩阵乘法**：编写一个函数来计算两个矩阵的乘积。这个函数将用于后续的矩阵幂运算。
3. **快速幂算法**：
   - 初始化结果矩阵为 identity matrix（单位矩阵），即对于任何矩阵 A，A^0 = I。
   - 将指数 n 转换成二进制形式。
   - 从最低位开始，对于每个二进制位：
     - 如果该位为 1，则将结果矩阵与当前的基矩阵幂乘积相乘。
     - 将基矩阵平方（即基矩阵乘以自身）。
     - 移动到下一个二进制位。
   - 当所有二进制位都被处理过后，结果矩阵就是原始矩阵的 n 次幂。
4. **结果提取**：对于斐波那契数列，结果矩阵的第一个元素（[0][0]）就是第 n 个斐波那契数。
矩阵快速幂的关键在于，每次迭代都将指数减半，因此迭代次数是对数级别的。这种方法非常适合计算大数的幂运算，不仅用于斐波那契数列，还广泛应用于其他需要矩阵幂运算的场景。

