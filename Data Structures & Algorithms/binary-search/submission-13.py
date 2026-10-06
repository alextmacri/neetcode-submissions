class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Lower and upper bounds (nums is sorted) are inclusive, so we can use
        #   property in our loop logic. Since low_i and up_i are valid indices
        #   any index between them will be valid as well
        low_i = 0
        up_i = len(nums) - 1

        # Keep looping until you converge to one valid index (above property,
        #   any index between low_i and up_i is also valid, and as you can see
        #   in the loop below, low_i and up_i are always between the original
        #   bounds)
        while low_i < up_i:
            # Get midpoint between lower and upper bounds (don't forget to
            #   put it on top of low, since you already ruled out what's
            #   below that)
            mid_i = (up_i - low_i) // 2 + low_i
            
            if nums[mid_i] == target:
                # Lucky you
                return mid_i
            elif nums[mid_i] < target:
                # Midpoint is smaller than target, so we eliminate the first
                #   (smaller) half of the array. Since the lower and upper
                #   bounds are inclusive, we have to get rid of the midpoint
                #   itself as well, since that was already seen to be smaller
                #   than the target, i.e. invalid. This way also helps prevent
                #   infinite loops
                low_i = mid_i + 1
            else:
                # Midpoint is larger than target, get rid of the second
                #   (larger) half of the array, inclusively
                up_i = mid_i - 1
        
        # Final check on the last valid index, then return value for not found
        return low_i if nums[low_i] == target else -1