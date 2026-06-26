class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cost = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_cost:
                min_cost = price
            
            profit = price - min_cost

            max_profit = max(profit, max_profit)
        
        return max_profit