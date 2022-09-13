class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for r in range(1, len(triangle)):
            for c in range(r+1):
                if c == 0:
                    triangle[r][c] += triangle[r-1][c]
                    
                elif c == r:
                    triangle[r][c] += triangle[r-1][c-1]
                    
                else:
                    triangle[r][c] += min(triangle[r-1][c-1], triangle[r-1][c])
                    
        return min(triangle[len(triangle) - 1])
