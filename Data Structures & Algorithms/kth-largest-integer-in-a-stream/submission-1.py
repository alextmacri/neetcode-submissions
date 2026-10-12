import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # For this, we get full control over what data structure we use as new
        #   values come in. Another way of saying "kth-largest" is "smallest of
        #   the k largest", which means we could keep track of the k largest
        #   in a way that makes it easy to keep track of and get the smallest
        #   of those, and whenever we add one, we add it and if it's in the
        #   new top k then we keep it there and get rid of the smallest,
        #   otherwise we get rid of it
        # Best way to keep track of a set of numbers and reliably-quiclky keep
        #   track of and get the smallest of those is a Min-Heap
        self.k = k
        self.min_heap = []
        
        for num in nums:
            self._append_max_k(num)
    
    def _append_max_k(self, val: int) -> None:
        # Mutate the Min-Heap to append, popping if there are more than k to
        #   preserve the property that the Min-Heap represents "the min of the
        #   max k elements". This works because if it's the smallest of the
        #   Min-Heap (i.e. not in the top k), then it gets bubbled all the way
        #   up and popped off, and if it's not the smallest (i.e. in the top
        #   k), then it stays in there, and a new kth-largest is decided after
        #   the smallest gets popped (maybe the new element, maybe another
        #   one)
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        self._append_max_k(val)
        return self.min_heap[0]
