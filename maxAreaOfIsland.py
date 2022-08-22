class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        total , self.adder = 0 , 0
        def dfs(newRow , newCol):
           
            if newCol == m or newRow == n or newCol < 0 or newRow < 0  or (newRow , newCol) in visited: 
                return
            
            if grid[newRow][newCol] == 0:
                visited.add((newRow , newCol))
                return
            
            visited.add((newRow,newCol))
            self.adder += 1
            dfs(newRow + 1 , newCol)
            dfs(newRow - 1 , newCol)
            dfs(newRow , newCol + 1)
            dfs(newRow , newCol - 1)
            
        visited = set()
        for row in range(n):
            for col in range(m):
                self.adder = 0
                if (row , col) not in visited:
                    dfs(row , col)
                    total = max(total , self.adder)
        print(len(visited))             
        return total                  
