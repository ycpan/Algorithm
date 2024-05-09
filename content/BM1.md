# 反转链表
## 问题
**描述**
给定一个单链表的头结点pHead(该头节点是有值的，比如在下图，它的val是1)，长度为n，反转该链表后，返回新链表的表头。

如当输入链表{1,2,3}时， 经反转后，原链表变为{3,2,1}，所以对应的输出为{3,2,1}。

**示例1**
```
输入：
{1,2,3}
返回值：
{3,2,1}
```
**示例2**
```
输入：
{}
返回值：
{}
说明：
空链表则输出空
```
## 解答
链表反转在不改变链表的情况下，就是要把链表进行拆开，分成前后两部分，前部分进行反转，后部分依次赋值给前部分，最终完成整个链表的反转。需要分成四步:    

0. 新设`pre`,表示当前反转后的链表的入口.还没反转之前，设为None，表示当前入口为None，也就是没有入口
1. 将当前`head`的`next` node赋值给`temp`，防止丢失,即`temp = head.next`
2. 将当前`head`与`next`进行断开，并赋值给`pre`,进行反转,即`head.next = pre`
3. 将(旧的)`head`赋值给`pre`,代表当前的反转入口，已经更新的`head`节点位置，即`pre = head`
4. 将拆开后最新开始位置的入口(`temp`)赋值给`head`,表示新的`head`已经更新，即`head = temp`
```python
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre

if __name__ == '__main__':

    head1 = ListNode(1)
    head2 = ListNode(2)
    head3 = ListNode(3)
    head1.next = head2
    head2.next = head3
    st = Solution()
    s = st.ReverseList(head1)
    print(s.val)
    print(s.next.val)
    print(s.next.next.val)
```
