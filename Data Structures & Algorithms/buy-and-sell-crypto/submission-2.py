class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        profit = 0


        for i in range(len(prices)):
            curr = prices[i]
            if curr < min_price:
                min_price = curr
            for j in range(i+1, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        
        return profit


            
            


        