import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first == second:
                continue
            else:
                heapq.heappush(heap, -(first - second))
        if len(heap) == 0: return 0
        return abs(heap[0])