from typing import List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 创建一个虚拟头节点，方便操作
        dummy = ListNode(0)
        current = dummy
        # 初始化优先队列
        heap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        # 循环直到优先队列为空
        while heap:
            # 取出最小节点
            _,_, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            # 将取出的节点的后继节点加入优先队列
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
        
        return dummy.next

# Example usage:
# Create linked lists: 1->4->5, 1->3->4, 2->6
lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]

# Merge the linked lists
solution = Solution()
merged_head = solution.mergeKLists(lists)

# Print the merged linked list
current = merged_head
while current:
    print(current.val, end=" -> ")
    current = current.next
# Output should be: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

