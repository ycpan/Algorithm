import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []  # 大顶堆，存储较小的一半元素
        self.min_heap = []  # 小顶堆，存储较大的一半元素

    def addNum(self, num: int) -> None:
        # 如果大顶堆为空或num小于等于大顶堆的堆顶元素，将num添加到大顶堆
        import ipdb
        ipdb.set_trace()
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # 平衡两个堆的大小
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]

# 示例
medianFinder = MedianFinder()
medianFinder.addNum(-1)    # arr = [-1]
print(medianFinder.findMedian()) # 返回 -1.0
medianFinder.addNum(-2)    # arr = [-1, -2]
print(medianFinder.findMedian()) # 返回 -1.5
medianFinder.addNum(-3)    # arr = [-1, -2, -3]
print(medianFinder.findMedian()) # 返回 -2.0
medianFinder.addNum(-4)    # arr = [-1, -2, -3, -4]
print(medianFinder.findMedian()) # 返回 -2.5
medianFinder.addNum(-5)    # arr = [-1, -2, -3, -4, -5]
print(medianFinder.findMedian()) # 返回 -3.0

