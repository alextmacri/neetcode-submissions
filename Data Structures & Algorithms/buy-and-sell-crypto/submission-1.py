class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMaxProfit = 0
        currentMinPrice = prices[0]
        currentMaxPrice = prices[0]

        for price in prices[1:]:
            if price < currentMinPrice:
                currentMinPrice = price
                currentMaxPrice = price
            elif price > currentMaxPrice:
                currentMaxPrice = price

                if currentMaxPrice - currentMinPrice > currentMaxProfit:
                    currentMaxProfit = currentMaxPrice - currentMinPrice
        
        return currentMaxProfit