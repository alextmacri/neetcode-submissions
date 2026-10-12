class Solution:
    def climbStairs(self, n: int) -> int:
        # For this, since we can only go up by 1 or 2 steps at a time, that
        #   means the ONLY 2 ways we can continue up is by going up 1 step
        #   from the step below, or by going up 2 steps from the step 2 below,
        #   which means it's just the amount of ways to get to the step 1
        #   below + the amount of ways to get to the step 2 below (DYNAMIC
        #   PROGRAMMING)
        # Since this is somewhat simple, we will do a bottom-up iterative
        #   approach to solving this, where we defined the base case first,
        #   then get to the final answer with a loop, calculating the results
        #   of the subproblems along the way using previous subproblem results
        #   (or base case results)
        
        # Edge case: n is 1 or 2 (the subproblem base cases):
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        prev_1 = 2
        prev_2 = 1

        for _ in range(3, n + 1):
            current = prev_1 + prev_2
            prev_1, prev_2 = current, prev_1
        
        return current