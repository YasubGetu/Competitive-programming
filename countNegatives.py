class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count , colPtr , rowPtr = 0 , 0 , len(grid) - 1
        
        while colPtr < len(grid[0]) and rowPtr > -1:
            if grid[rowPtr][colPtr] >= 0:
                colPtr += 1
            else:
                count += len(grid[0]) - colPtr
                rowPtr -= 1
                
        return count      
