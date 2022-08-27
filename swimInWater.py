class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        direction = [[1,0] , [0,1] , [-1,0] , [0,-1]]
        n = len(grid)
        minH = [[grid[0][0] , 0 , 0]]
        visited.add((0,0))
        while minH:
            t,r,c = heapq.heappop(minH)
            if (r , c) == (n-1 , n-1):
                    return t
            for direct in direction:
                nr , nc = r + direct[0] , c + direct[1]
                if nr >= n or nc >=n or nc < 0 or nr < 0 or (nr , nc) in visited:
                    continue
                visited.add((nr,nc))
                heapq.heappush(minH, [max(t,grid[nr][nc]) , nr , nc])
                
