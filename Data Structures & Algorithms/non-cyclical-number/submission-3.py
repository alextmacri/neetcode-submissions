class Solution:
    def _sum_of_squares(self, n: int) -> int:
        # Helper function to get sum of squares whatever
        total = 0

        while n > 0:
            total += (n % 10) ** 2
            n //= 10

        return total

    def isHappy(self, n: int) -> bool:
        n_so_far = set()

        while n != 1:
            if n in n_so_far:
                return False
            
            n_so_far.add(n)

            n = self._sum_of_squares(n)

        return True