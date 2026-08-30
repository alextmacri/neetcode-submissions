class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        for i in range(len(nums)):
            n = nums[i]

            if n in differences:
                return [differences[n], i]
            else:
                differences[target - n] = i