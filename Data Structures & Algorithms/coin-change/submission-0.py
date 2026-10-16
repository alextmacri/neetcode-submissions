class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # To get the fewest number of coins to make a value, you can just get
        #   the lowest amount to make the full amount minus each denomination
        #   you have access to (making it the lowest amount + 1). This will
        #   take O(n * t) time where n is the amount and t is the # of
        #   denominations we have. I'm convinced we can't do better here since
        #   _

        # First, populate the list with -1 until the first actual amount we
        #   can make (we can do it like this since all coins are 1 or more, so
        #   it's guarunteed that the first amount we can make at all is the
        #   lowest value of coins, and we're indexing the amounts list as
        #   the index being the amount - 1, since the denominations start at 1
        #   so recording 0 as an amount would be useless, and it makes working
        #   with the indexes a bit easier in the loop)
        amounts = [0]

        # Now, do the loop (bottom-up approach since we can easily map it
        #   out). Want to start right after the min coin, and want the last
        #   value we work with to be the amount
        for curr_amount in range(1, amount + 1):
            amount_choices = []

            for coin in coins:
                prev_amount = curr_amount - coin
                if prev_amount >= 0 and amounts[prev_amount] > -1:
                    amount_choices.append(amounts[prev_amount] + 1)
            
            amounts.append(min(amount_choices) if amount_choices != [] else -1)

        return amounts[amount]