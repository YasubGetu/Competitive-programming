class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        queue = []
        fresh = time = 0
        directions = [ [1,0] , [0,1] , [-1,0] , [0,-1] ]
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append([row , col])
                    
        while queue and fresh > 0:
            for i in range(len(queue)):
                r , c = queue.pop(0)
                for direc in directions:
                    nr , nc = r + direc[0] , c + direc[1]
                    if nr == n or nc == m or nr < 0 or nc < 0 or grid[nr][nc] != 1:
                        continue
                    queue.append((nr,nc))
                    grid[nr][nc] = 2
                    fresh -= 1
            time += 1 
            
        return time if fresh == 0 else -1     
