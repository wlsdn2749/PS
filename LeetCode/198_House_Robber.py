from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
        return dp[-1]
    
s = Solution()
print(s.rob(nums=[1,2,3,1]))
print(s.rob([2,7,9,3,1]))


            
            