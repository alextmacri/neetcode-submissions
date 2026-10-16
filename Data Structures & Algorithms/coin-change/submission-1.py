class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # To get the fewest number of coins to make a value, you can just get
        #   the lowest amount to make the full amount minus each denomination
        #   you have access to (making it the lowest amount + 1). This will
        #   take O(n * t) time where n is the amount and t is the # of
        #   denominations we have

        # First, initialize the list that will be the amount of coins needed
        #   for an amount of that index, starting with the base case as
        #   described in the question text (0). I originally tried to
        #   auto-populate until the list starts with -1, but decided not to as
        #   it doesn't really save much time and adds more complexity to the
        #   algorithm than it's worth
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