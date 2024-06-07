from typing import List
from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(y, x, cur_word):
            # print(cur_word)
            
            if cur_word == word:
                return True
            
            dx = [1,0,-1,0]
            dy = [0,-1,0,1]
            
            for i in range(4):
                ddy = y + dy[i]
                ddx = x + dx[i]
                
                if 0 <= ddx < len(board[0]) and 0 <= ddy < len(board):
                    if visited[ddy][ddx] == 0 and word[len(cur_word)] == board[ddy][ddx]:
                        visited[ddy][ddx] = 1
                        if dfs(ddy, ddx, cur_word + board[ddy][ddx]):
                            return True
                        visited[ddy][ddx] = 0 
                        
            return False

        visited = [ [0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    if dfs(i,j,word[0]):
                        return True
                    
                    visited[i][j] = 0
                    
        
        return False
    
                    
s = Solution()
print( s.exist(board=[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], word="ABCESEEEFS") )
# print(s.exist(board=[["a","a"]], word="aaa"))