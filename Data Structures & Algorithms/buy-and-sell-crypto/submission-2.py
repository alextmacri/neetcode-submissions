class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize info I'll need to keep track of
        currentMaxProfit = 0
        currentMinPrice = prices[0]
        currentMaxPrice = prices[0]

        # I will need to loop through the rest of the days to see what's up
        for price in prices[1:]:
            # If there is a new lowest price, keep track of old max profit
            #   and start keeping track from here. No need for recursion or
            #   a nested loop since the "old" max profit is kept for comparison,
            #   and any new max found after it is guarunteed to make a better
            #   profit with this new min price
            if price < currentMinPrice:
                currentMinPrice = price
                currentMaxPrice = price
            # If the price is a new max, make it current max and see if it
            #   hits the "global" max profit as well
            elif price > currentMaxPrice:
                currentMaxPrice = price

                if currentMaxPrice - currentMinPrice > currentMaxProfit:
                    currentMaxProfit = currentMaxPrice - currentMinPrice
        
        return currentMaxProfit