#描述
#给定一个单链表的头结点pHead(该头节点是有值的，比如在下图，它的val是1)，长度为n，反转该链表后，返回新链表的表头。
#如当输入链表{1,2,3}时，
#经反转后，原链表变为{3,2,1}，所以对应的输出为{3,2,1}。
#以上转换过程如下图所示：
#
#示例1
#输入：
#{1,2,3}
#复制
#返回值：
#{3,2,1}
#复制
#示例2
#输入：
#{}
#复制
#返回值：
#{}
#复制
#说明：
#空链表则输出空
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
#def input_trans(li):
#    output = []
#    for i in range(0,len(li) - 1):
#        ListNode()

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
