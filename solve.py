class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n , m = len(board) , len(board[0])
        def dfs(r , c):
            if r >= n or r < 0 or c >= m or c < 0 or board[r][c] != "O":
                return
            board[r][c] = "K"
            dfs(r + 1 , c)
            dfs(r - 1 , c)
            dfs(r , c + 1)
            dfs(r , c - 1)
            
        for row in range(n):
            for col in range(m):
                if (row in [0 , n - 1] or col in [0 , m - 1]) and board[row][col] == "O":
                    dfs(row , col)
                    
        for row in range(n):
            for col in range(m):
                if board[row][col] == "O":
                    board[row][col] = "X"
                    
        for row in range(n):
            for col in range(m):
                if board[row][col] == "K":
                    board[row][col] = "O"
