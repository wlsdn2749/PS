from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        out_region = lambda y,x: x == 0 or x == len(board[0])-1 or y == 0 or y == len(board) -1
        
        
        def bfs(i, j):
            dq = deque()
            regions = list()
            is_surrounded = True
            
            dq.append((i, j))
            visited[i][j] = 1
            
            while dq:
                y, x = dq.popleft()
                if out_region(y,x):
                    is_surrounded = False
                    
                regions.append((y, x))
                
                for k in range(4):
                    ddy = y + dy[k]
                    ddx = x + dx[k]
                    
                    
                    if 0 <= ddx < len(board[0]) and 0 <= ddy < len(board):
                        if not visited[ddy][ddx] and board[ddy][ddx] == 'O':
                            dq.append((ddy, ddx))
                            visited[ddy][ddx] = 1
                            
            if is_surrounded:
                for y,x in regions:
                    board[y][x] = 'X'                
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not visited[i][j] and board[i][j] == 'O':
                    bfs(i, j)
                
    
# s = Solution()
# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# s.solve(board)
# [print(board[i]) for i in range(len(board))]
# board = [["X"]]
# s.solve(board)
# [print(board[i]) for i in range(len(board))]

