class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n , m = len(board) , len(board[0]) 
        DIR = [(0,1), (0,-1), (1, 0),(-1,0), (1,1),(1,-1),(-1,1),(-1,-1)]
        x , y = click
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
     
        def dfs(r , c):
            if r >= n or c >= m or r < 0 or c < 0 or board[r][c] == "B" or board[r][c].isnumeric():
                return

            count = 0
            for direction in DIR:
                newR , newC = r + direction[0] , c + direction[1]
                if newR < 0 or newC < 0 or newR >= n or newC >= m or board[newR][newC] != "M":
                    continue
                count += 1    
            if count:            
                board[r][c] = str(count)
            else:
                board[r][c] = "B"
                for direction in DIR:
                    newR , newC = r + direction[0] , c + direction[1]
                    if newR < 0 or newC < 0 or newR >= n or newC >= m:
                        continue
                    dfs(newR,newC)
        dfs(x , y)
        return board
