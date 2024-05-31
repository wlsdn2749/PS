from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def horizontal_check():
            
            for row in board:
                dd = defaultdict(int)
                for i in row:
                    if i == ".":
                        continue
                    
                    dd[i] += 1
                    
                    if dd[i] >= 2:
                        return False
                    
            return True
                    
                
        def vertical_check():
            
            for i in range(9):
                dd = defaultdict(int)
                for j in range(9):
                    if board[j][i] == ".":
                        continue
                    dd[ board[j][i] ] += 1
                    
                    if dd [board[j][i]] >= 2:
                        return False
                    
            return True
        
        def square_check():
            
            for i in [0, 3, 6]:
                for j in [0, 3, 6]:
                    dd = defaultdict(int)
                    
                    for y in range(3):
                        for x in range(3):
                            
                            if board[i+y][j+x] == ".":
                                continue    
                            dd [ board[i+y][j+x] ] += 1
                            
                            if dd[ board[i+y][j+x] ] >= 2:
                                return False
                            
            return True
            
        # print(horizontal_check())
        # print(vertical_check())
        # print(square_check())
        return horizontal_check() and vertical_check() and square_check()
        
        
s = Solution()
# board1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# board2 = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

board3 = [[".",".",".",".",".",".","5",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          ["9","3",".",".","2",".","4",".","."],
          [".",".","7",".",".",".","3",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".","3","4",".",".",".","."],
          [".",".",".",".",".","3",".",".","."],
          [".",".",".",".",".","5","2",".","."]]
print( s.isValidSudoku(board3) )


