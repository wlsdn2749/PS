class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [0 for _ in range(n+1)]
        
        square_set = set(i**2 for i in range(int(n**0.5 + 1)))
        
        for i in range(1, n+1): 
            
            if i in square_set:
                dp[i] = 1
                
            else:
                dp[i] = self.getMaximumSquares(i, dp)
        
        return dp[n]
    
    def getMaximumSquares(self, s, dp):
        
        iter_val = 1
        max_count = 10000
        
        while True:
            if s - iter_val ** 2 > 0:
                max_count = min(max_count, 1 + dp[s - iter_val ** 2])
                iter_val += 1
            else:
                break
            
        return max_count
            
            

s = Solution()
print(s.numSquares(n = 12))
print(s.numSquares(n = 13))