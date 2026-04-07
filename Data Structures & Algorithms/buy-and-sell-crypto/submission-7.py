class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            profit = 0
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l] 
            else:
                l  = r
                
            if profit > max_profit:
                max_profit = profit
            r += 1
        return max_profit


