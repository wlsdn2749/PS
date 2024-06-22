from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        max_value = amount + 1
        dp = [max_value] * max_value
        
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, max_value):
                dp[x] = min(dp[x], dp[x - coin] + 1)
                
        return dp[amount] if dp[amount] != max_value else -1
        


s = Solution()
result = s.coinChange(coins=[1,2,5], amount=11)
print(result)
            
    