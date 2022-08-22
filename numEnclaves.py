class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        count = 0
        
        def dfs(r , c):
            if r == n or r < 0 or c == m or c < 0 or grid[r][c] != 1:
                return 
            grid[r][c] = 0
            dfs(r , c + 1)
            dfs(r , c - 1)
            dfs(r + 1 , c)
            dfs(r - 1 , c)
            
        for row in range(n):
            for col in range(m):
                if (row in [0 , n - 1] or col in [0 , m - 1]) and grid[row][col] == 1:
                    dfs(row , col)
                    
        for row in range (n):
            for col in range(m):
                if grid[row][col] == 1:
                    count += 1
                    
        return count            
