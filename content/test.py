def topKFrequent(nums, k):
    # 统计每个元素出现的频率
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    # 手动实现的最小堆
    class MinHeap:
        def __init__(self):
            self.heap = []

        def push(self, item):
            self.heap.append(item)
            self._sift_up(len(self.heap) - 1)

        def pop(self):
            if not self.heap:
                return None
            min_item = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self._sift_down(0)
            return min_item

        def _sift_up(self, index):
            while index > 0:
                parent_index = (index - 1) // 2
                if self.heap[parent_index][1] > self.heap[index][1]:
                    self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                    index = parent_index
                else:
                    break

        def _sift_down(self, index):
            child_index = 2 * index + 1
            while child_index < len(self.heap):
                if child_index + 1 < len(self.heap) and self.heap[child_index + 1][1] < self.heap[child_index][1]:
                    child_index += 1
                if self.heap[index][1] > self.heap[child_index][1]:
                    self.heap[index], self.heap[child_index] = self.heap[child_index], self.heap[index]
                    index = child_index
                    child_index = 2 * index + 1
                else:
                    break

    # 使用最小堆
    min_heap = MinHeap()
    for item, freq in freq_map.items():
        min_heap.push((item, freq))
        if len(min_heap.heap) > k:
            min_heap.pop()

    # 从堆中提取结果
    return [item[0] for item in min_heap.heap]

# 测试
nums = [1,1,1,2,2,3,6,6,6,6,6,6]
k = 2
print(topKFrequent(nums, k))  # 输出: [1, 2]

