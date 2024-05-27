from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def backtracking(parentheses, left, right):
            if left == right == n:
                result.append(parentheses)
                return

            if left > right:
                backtracking(parentheses + ")", left, right+1)
                
            if left <= n and right <= n:
                backtracking(parentheses + "(", left+1, right)

        backtracking("(", 1, 0)
        
        return result


s = Solution()
print( s.generateParenthesis(3) )