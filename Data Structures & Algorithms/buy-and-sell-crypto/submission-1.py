class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        if n == 1 or n>10000:
            return 0
        
        start = 0
        for i in range(n-1):
            curr_profit =  max(prices[start+1:]) - prices[start] 
            max_profit=max(max_profit, curr_profit)
            start +=1
        return max_profit
