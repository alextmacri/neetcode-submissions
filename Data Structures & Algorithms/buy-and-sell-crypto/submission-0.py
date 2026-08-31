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
                newMaxProfit = currentMaxPrice - currentMinPrice

                if newMaxProfit > currentMaxProfit:
                    currentMaxProfit = newMaxProfit
        
        return currentMaxProfit