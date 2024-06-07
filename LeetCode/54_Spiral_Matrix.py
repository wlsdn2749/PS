from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:            
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = [*zip(*matrix)][::-1]
        return res


s = Solution()
print( s.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]) )