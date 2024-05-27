def _parent(i):
    return (i - 1) // 2
def _swap(heap,i,j):
    heap[i],heap[j] = heap[j],heap[i]
def _left_child(i):
    return 2 * i + 1
def _right_child(i):
    return 2 * i + 2
def _has_left_child(heap,i):
    return _left_child(i) < len(heap)
def _has_right_child(heap,i):
    return _right_child(i) < len(heap)
def insert(heap,val):
    heap.append(val)
    i = len(self.heap) - 1
    while i > 0 and heap[_parent(i)] >  heap[i]:
        _swap(i,_parent(i))
        i = _parent(i)
def extract_min(heap):
    if len(heap) == 0:
        raise Exception('Heap is empty')
    min_val = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    i = 0
    while _has_left_child(i):
        min_child_idx = _left_child(i)
        if _has_right_child(i) and heap[_right_child(i) < heap[_left_child(i)]:
            min_child_idx = _right_child(i)
        if heap[i] < heap[min_child_idx]:
            break
        _swap(i,min_child_idx)
        i = min_child_idx
    return min_val
def nlargest(heap,k):
    if k <= 0:
        raise ValueError('k should greater than 0')
    if k >= len(heap):
        return heap
    res = []
    i = 0
    while i < k:
        min_val = extract_min(heap)
        res.append(min_val)
    return res

