class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        so_far = set()

        for n in nums:
            if n in so_far:
                return True
            else:
                so_far.add(n)
        
        return False