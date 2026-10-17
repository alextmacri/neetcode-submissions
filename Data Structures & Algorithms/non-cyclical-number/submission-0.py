class Solution:
    def _sum_of_squares(self, n: int) -> int:
        # Helper function to get sum of squares whatever
        digits = [int(d) for d in str(n)]
        return sum(d ** 2 for d in digits)

    def isHappy(self, n: int) -> bool:
        # For this, we need to keep getting it until we either get to 1 or
        #   find that it's cyclical. To do this, we could keep track
        n_so_far = set()

        while n != 1:
            if n in n_so_far:
                return False
            
            n_so_far.add(n)

            n = self._sum_of_squares(n)

        return True