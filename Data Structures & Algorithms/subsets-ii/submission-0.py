class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        For this we will do a backtracking approach with the leaves being
        all possibilities of the potential choices to make (i.e. whether to
        include or not include a given element in the subset). So, we will
        make the following choice at every item in nums: do we include this
        item in the subset? This will produce all possible subsets. We then
        have to find a way to disqualify the duplicates, for this our best
        choices are to maintain a set of unique additions to the list, or
        prevent the choice of including the same value to be made. The first
        option will take an extra O(2^n) set, which isn't ideal. For the
        second option, we can either keep a set for what has been used so far
        or sort and check if it's the same as the previous one. The first
        option will take an extra O(n) set, which isn't ideal, but the second
        option will take a O(n log n) step near the beginning, so I'll go with
        that instead.
        """
        # Sort the input array (so that equal values come after each other,
        #   our method of preventing duplicate subsets)
        nums.sort()

        # The final state that we edit to collect the leaves/results of all
        #   choices made
        subsets = []

        # The actual backtracking
        def _backtrack(index: int, subset: list[int], prev_add: bool) -> None:
            """
            The recursive DFS Backtracking algorithm, where we add the leaf
            nodes to the overall solution list.
            """
            # Base Case: we have reached the end of the list (all choices
            #   have been made => leaf node)
            if index >= len(nums):
                # Add to overall solution list and return
                subsets.append(subset)
                return
            
            # Choice 1: add it to the list if it wasn't already
            _backtrack(index + 1, subset + [nums[index]], True)

            # Backtrack
            # (This is handled implicitly since our current state is copied
            #   and given to the recursive call insetad of being modified
            #   directly in the recursive call, so the changes we make further
            #   down in the tree are not in the state in at this level)

            # Choice 2: don't add it to the list
            if index < 1 or nums[index] > nums[index - 1] or not prev_add:
                _backtrack(index + 1, subset, False)

        _backtrack(0, [], False)
        return subsets