class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, start, end = 0, 0, 1
        n = len(prices)
        while start < n and end < n:
            if prices[start] < prices[end]:
                ans = max(ans, prices[end] - prices[start])
                
            else:
                start = end
                
            end += 1
                
        return ans
