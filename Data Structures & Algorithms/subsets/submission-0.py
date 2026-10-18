class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        For this, we could just iterate through and add a copy of all existing
        subsets to the subset list but with the next item (starting with an
        empty list), doubling the amount of subsets each time until we get to
        a total of 2^n subsets (after n iterations of at most 2^n operations,
        since we have to double the amount each time until the end). But, this
        isn't as extensible as a recursive backtracking approach, so we will
        be doing that instead even though recursion means we need extra memory
        for the stack frames and may run into stack overflow (I usually like
        to avoid this, but this is a learning experience).

        For a backtracking approach, we can see the subsets as nodes of a tree
        with the empty list as the root, and each leaf node (full set of
        choices made, e.g. what is included in that subset) is part of the
        output of possible subsets. WE BUILD THE TREE RECURSIVELY AS WE
        TRAVERSE IT WITH DFS, AND WHEN WE GO BACK UP A RECURSIVE CALL, THAT'S
        CALLED "BACKTRACKING". In this case we start with an empty list, and
        as we traverse down, we have CHOICE 1 be not adding the current
        element to the subset, and CHOICE 2 be adding it to the current
        subset, and all leaf nodes (i.e. when the entire domain has been acted
        upon) are the possible subsets, since they were all built from unique
        decision paths. Since we are making 2 choices for every item in the
        original list, it is O(n * 2^n) steps, and throughout that we're
        updating the same list that grows to size 2^n with its elements
        reaching size n at most, and we recurse to a max depth of 2^n, meaning
        it will be O(n * 2^n) space.
        """
        all_subsets = []

        def _backtrack(index: int, subset: list[int]) -> None:
            """
            Backtracking helper function to append subsets from the end of all
            branching "Choice Paths". We are doing the index and not the item
            itself as one of the arguments because that makes it easier to
            detect the Base Case (the entire list has been gone through => all
            Choices have been made).
            """
            nonlocal all_subsets, nums

            # Base Case: we are at the end of the input list (all choices
            #   have been made), so we can finally return the fully made
            #   "possibility" and return
            if index >= len(nums):
                all_subsets.append(subset)
                return

            # Choice 1: include the item at this index in the subset
            _backtrack(index + 1, subset + [nums[index]])

            # BACKTRACK BETWEEN CHOICE AS WE RETURN FROM RECURSION

            # (This is handled implicitly because we pass a copy of the
            #   current subset with the addition to it instead of MODIFYINg
            #   the one we're currently using)

            # Choice 2: don't include the item at this index in the subset
            _backtrack(index + 1, subset)
        
        _backtrack(0, [])
        return all_subsets