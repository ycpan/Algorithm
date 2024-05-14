class MinHeap:
    def __init__(self):
        self.heap = []
    def parent(self, i):
        return (i - 1) // 2
    def left_child(self, i):
        return 2 * i + 1
    def right_child(self, i):
        return 2 * i + 2
    def has_left_child(self, i):
        return self.left_child(i) < len(self.heap)
    def has_right_child(self, i):
        return self.right_child(i) < len(self.heap)
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    def extract_min(self):
        if len(self.heap) == 0:
            raise Exception("Heap is empty")
        min_val = self.heap[0]
        # Move the last item in the heap to the root and heapify
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        i = 0
        while self.has_left_child(i):
            min_child_idx = self.left_child(i)
            if (self.has_right_child(i) and
                    self.heap[self.right_child(i)] < self.heap[self.left_child(i)]):
                min_child_idx = self.right_child(i)
            if self.heap[i] < self.heap[min_child_idx]:
                break
            self.swap(i, min_child_idx)
            i = min_child_idx
        return min_val
# 使用小根堆
min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(1)
min_heap.insert(4)
min_heap.insert(1)
min_heap.insert(5)
print("Extracted:", min_heap.extract_min())  # 应该输出 1
print("Extracted:", min_heap.extract_min())  # 应该输出 1
print("Extracted:", min_heap.extract_min())  # 应该输出 3
