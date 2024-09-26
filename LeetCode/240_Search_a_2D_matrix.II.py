from typing import List, Optional
from collections import deque


# Version 1. BFS, Visited
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_idx_x = len(matrix[0]) // 2
        start_idx_y = len(matrix) // 2
        dq = deque()
        visited = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        dq.append((start_idx_y, start_idx_x))
        visited[start_idx_y][start_idx_x] = 1
        
        def add(y, x):
            if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
                if not visited[y][x]:
                    dq.append((y,x))
                    visited[y][x] = 1
            
            
        while dq:
            y, x = dq.popleft()
            
            if matrix[y][x] == target:
                return True
            
            if matrix[y][x] < target:
                add(y+1, x)
                add(y, x+1)
                
            elif matrix[y][x] > target:
                add(y-1, x)
                add(y, x-1)
        
        return False
    
    

# Version 2. Linear Search Top-Right Corner Approach
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            
            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] < target:
                row += 1
            
            elif matrix[row][col] > target:
                col -= 1
            
        
        return False
        

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
s = Solution()
print(s.searchMatrix(matrix=matrix, target=target))
        