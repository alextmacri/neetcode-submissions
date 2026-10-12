import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        
        for num in nums:
            self._append_max_k(num)
    
    def _append_max_k(self, val: int) -> None:
        # Mutate the min heap to append, popping if there are more than k to
        #   preserve the property that the min heap represents "the min of the
        #   max k elements"
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        self._append_max_k(val)
        return self.min_heap[0]
