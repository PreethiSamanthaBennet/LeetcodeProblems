class Solution(object):
    def maxProfit(self, prices):
        minValue = 10000
        maxDifference = 0
        
        for i in range(len(prices)):
            minValue = min(prices[i], minValue)
            maxDifference = max(prices[i]-minValue, maxDifference)
            
        return maxDifference
