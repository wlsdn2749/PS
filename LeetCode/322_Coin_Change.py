from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [2**31-1 for _ in range(amount+1)]
        dp[0] = 0
        

        def bt(cur):
            if cur < 0:
                return 2**31-1
            
            if dp[cur] != 2**31 -1:
                return dp[cur]
            
            for i in range(len(coins)):
                result = bt(cur - coins[i]) + 1
                dp[cur] = min(dp[cur], result)
                
            return dp[cur]

        result = bt(amount)
        
        return result if result != 2**31-1 else -1
    
    
s = Solution()
result = s.coinChange(coins=[1], amount=0)
print(result)
            
    