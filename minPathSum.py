class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = [[float("inf")]* (m+1) for x in range(n+1)]
        res[0][1] = 0
        
        for r in range(1, n+1):
            for c in range(1, m+1):
                res[r][c] = grid[r-1][c-1] + min(res[r-1][c], res[r][c-1])
                       
        return res[n][m]
