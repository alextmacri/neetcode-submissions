class Solution:
    def _targetTwoSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Helper function that gets all indexes where i != j and their values add
        up to the given target. This takes time O(n) and space O(n), since we
        only iterate through the list once and also use a hashmap that grows to
        size n. Will return empty list if there are none that add up to target.
        """
        valid_sums = []
        nums_so_far = set()

        i = 0
        while i < len(nums):
            num = nums[i]
            difference = target - num

            if difference in nums_so_far:
                # Guarunteed that i != j since i isn't in nums_so_far yet
                valid_sums.append([num, difference])
                nums_so_far.remove(difference)
            else:
                nums_so_far.add(num)
            
            # Skip to second last iteration of this, so that we can catch the
            #   case of multiple adding up to it, without blowing up the output
            #   with copies of the same over and over (e.g. 0's)
            while i + 2 < len(nums) and nums[i] == nums[i + 1] == nums[i + 2]:
                i += 1

            i += 1
        
        return valid_sums

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        For this, we can break the problem up in to smaller pieces and see that
        every sum of 3 is really just the sum of 2, where one of those is the
        sum of another 2 numbers. From here, we can use our efficient two sum
        solution to simplify it, making it O(n^2) time and O(n) space. The
        hidden hard part is not containing any duplicates, for that we will
        sort and loop to skip the duplicates (faster and more memory-efficient
        than converting to set then back to list, and for that there is no
        extra space used and the runtime of sorting is dominated by the runtime
        of the rest).
        """
        nums.sort()

        valid_sums = []
        i = 0
        while i < len(nums):
            for target_sum in self._targetTwoSum(nums[i + 1:], -nums[i]):
                # Excluding all before means avoiding duplicates
                valid_sums.append(target_sum + [nums[i]])
            
            # Skip to last of its value
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            i += 1
        
        return valid_sums
