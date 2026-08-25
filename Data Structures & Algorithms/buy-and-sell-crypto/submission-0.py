class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Take a greedy approach
        # keep track of max profit
        # for each day, keep track of min behind it
        # take max profit

        best = 0
        lowest = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - lowest
            best = max(best, profit)
            lowest = min(lowest, prices[i])
        
        return best

            