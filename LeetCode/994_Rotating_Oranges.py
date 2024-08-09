from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        dq = deque()
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    dq.append((i, j, 0)) # (y,x)
        minutes = 0            
        while dq:
            y, x, minutes = dq.popleft()
            visited[y][x] = 1 
            
            for i in range(4):
                ddy = y + dy[i]
                ddx = x + dx[i]
                
                if 0 <= ddx < len(grid[0]) and 0 <= ddy < len(grid): # In range
                    if not visited[ddy][ddx] and grid[ddy][ddx] == 1: # 조건
                        dq.append((ddy, ddx, minutes+1))
                        grid[ddy][ddx] = 2
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
                        
        return minutes
                        
s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(s.orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]))
            
            
                
                
                
            
        