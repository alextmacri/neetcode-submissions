import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # We need to smash stones in order of weight, but the catch is that
        #   the stones get lighter after smashing if they survive, so we need
        #   to also have a way to re-order them to have it in order of weight,
        #   also we don't need to
        heapq.heapify_max(stones)

        curr_stone = heapq.heappop_max(stones)

        while len(stones) >= 1:
            curr_stone = abs(curr_stone - heapq.heappop_max(stones))
            heapq.heappush_max(stones, curr_stone)
            curr_stone = heapq.heappop_max(stones)

        return curr_stone