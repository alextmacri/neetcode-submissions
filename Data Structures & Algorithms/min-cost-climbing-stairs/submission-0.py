class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Since you can only take 1 or 2 steps at a time, the only way to get
        #   to a certain step is by taking 2 steps up from 2 steps below, or 1
        #   step up from 1 step below. This means that we can use these as
        #   SUBPROBLEMS and take an BOTTOM-UP (iterative) DYNAMIC PROGRAMMING
        #   approach to calculate as we traverse up. The base cases will be
        #   starting at 0 and starting at 1 as, and we will update the rest
        #   dynamically as we traverse up, recording the min cost for each
        #   step we go up until we finally can get the final answer at the
        #   end with one more check
        total_costs = cost[:2]

        for c in cost[2:]:
            total_costs.append(c + min(total_costs[-1], total_costs[-2]))

        return min(total_costs[-1], total_costs[-2])
