from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    
        def check_state(y, x):
            dy = [0,1,0,-1,1,1,-1,-1]
            dx = [1,0,-1,0,-1,1,-1,1]
            state = board[y][x]

            lives = 0
            dies = 0

            for idx in range(8):
                ddy = y + dy[idx]
                ddx = x + dx[idx]

                if 0 <= ddx < len(board[0]) and 0 <= ddy < len(board):
                    if board[ddy][ddx]: 
                        lives += 1 
                    else:
                        dies += 1

            if state == 1: # is live
                if lives < 2:
                    q.append((y,x,0))
                    
                elif lives == 2 or lives == 3:
                    q.append((y,x,1))

                elif lives > 3:
                    q.append((y,x,0))


            elif state == 0: # die
                if lives == 3:
                    q.append((y,x,1))
                    
        q = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                check_state(i, j)
                

        while q:
            y, x, state = q.pop()
            board[y][x] = state
            
        
                    
                    
s = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s.gameOfLife(board)

print(board)