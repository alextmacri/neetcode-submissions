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
        PRUNE THE FUTURE BRANCHES THAT WILL MAKE INVALID OUTPUTS (for us, this
        means pruning the future items with equal value after we go down the
        branch of including it, since we only need to go down one of those
        branches to get all of the possible unique output choices). The first
        option will take an extra O(2^n) set, which isn't ideal. For the
        second option, we can either keep a set for what has been used so far
        or sort and check if it's the same as the previous one. The first
        option will take an extra O(n) set, which isn't ideal, but the second
        option will take a O(n log n) step near the beginning, so I'll go with
        that instead.
        """
        # Sort the input array (so that equal values come after each other,
        #   so we can skip/prune branches that would lead to duplicates)
        nums.sort()

        # The final state that we edit to collect the leaves/results of all
        #   choices made
        subsets = []

        # The actual backtracking
        def _backtrack(index: int, subset: list[int]) -> None:
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
            
            # Choice 1: add it to the list
            _backtrack(index + 1, subset + [nums[index]])

            # Backtrack
            # (This is handled implicitly since our current state is copied
            #   and given to the recursive call insetad of being modified
            #   directly in the recursive call, so the changes we make further
            #   down in the tree are not in the state in at this level)

            # Prune: skip future branches that have the same value (we already
            #   went down the branch of including it, so we only need to go
            #   down the branch of not including it once, and prune the rest.
            #   So, we will skip past the same and do it at the last one, so
            #   we don't do it multiple times for the same value)
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            # Choice 2: don't add it to the list
            _backtrack(index + 1, subset)

        _backtrack(0, [])
        return subsets