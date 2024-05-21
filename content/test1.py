import heapq
class Node:
    def __init__(self,val = 0,next=None):
        self.val = val
        self.next = None
def merge_k(li):
    heap = []
    dummy = Node()
    current = dummy
    for i,head in enumerate(li):
        import ipdb
        ipdb.set_trace()
        heapq.heappush(heap,(head.val,i))
    while heap:
        val,idx = heapq.heappop(heap)
        node = li[idx]
        current.next = node
        current = current.next
        li[idx] = node.next
        if node.next:
            heapq.heappush(heap,(node.next.val,idx))
    return dummy.next
def create_lists(lst):
    dummy = Node()
    current = dummy
    for val in lst:
        current.next = Node(val)
        current = current.next
    return dummy.next
if __name__ == '__main__':
    lists = [[1,4,5],[1,3,4],[2,6]]
    lists_nodes = [create_lists(lst) for lst in lists]
    result = merge_k(lists_nodes)
    while result:
        print(result.val)
        result = result.next
