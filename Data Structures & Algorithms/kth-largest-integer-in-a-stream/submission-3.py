import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        for n in nums:
            heapq.heappush(self.min_heap, n)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        sorted_heap = sorted(self.min_heap)
        return sorted_heap[len(sorted_heap) - self.k]