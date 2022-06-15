class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = int(len(piles)/3)
        add = []
        x = 0
        sum = 0
        for i in range(n):
            add.append([piles[i] , piles[-x - 2] , piles [-x - 1]])
            sum += add[i][1]
            x += 2  
        return sum    
            
        
        
