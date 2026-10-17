class Solution:
    def _sum_of_squares(self, n: int) -> int:
        # Helper function to get sum of squares whatever
        total = 0

        while n > 0:
            total += (n % 10) ** 2
            n //= 10

        return total

    def isHappy(self, n: int) -> bool:
        """
        For this, we need to keep getting it until we either get to 1 or find
        that it's cyclical. As far as I know, there isn't a mathematical
        property that will allow us to get this info other than by recursively
        computing it and checking, while keeping track of what we've seen
        before (for this, the obvious choice is a set, since it has constant-
        time lookups). 
        """
        n_so_far = set()

        while n != 1:
            if n in n_so_far:
                return False
            
            n_so_far.add(n)

            n = self._sum_of_squares(n)

        return True