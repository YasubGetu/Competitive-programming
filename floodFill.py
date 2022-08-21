class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n , m = len(image) , len(image[0])
        startColor = image[sr][sc]
        def dfs (newRow , newCol):
            
            if newRow == n or newRow < 0 or newCol == m or newCol < 0  or image[newRow][newCol] == color or image[newRow][newCol] != startColor:
                return
            
            image[newRow][newCol] = color
            dfs(newRow + 1 , newCol)
            dfs(newRow - 1 , newCol)
            dfs(newRow , newCol + 1)
            dfs(newRow , newCol - 1)
                
        dfs(sr , sc)    
        return image
