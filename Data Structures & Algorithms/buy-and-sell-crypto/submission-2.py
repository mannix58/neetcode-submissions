class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,s = 0,1
        max_profit = 0

        while s < len(prices):
            profit = prices[s] - prices[b]
            if prices[s] < prices[b]:
                b += 1
            else:
                if profit > max_profit:
                    max_profit = profit
                s += 1
        
        return max_profit
        