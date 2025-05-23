from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Kadane's Algorithms [Dynamic Programming O(n)]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1]+nums[i])
            
        return max(nums) 
        
        
s = Solution()
print(s.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray(nums = [-2,-1]))
        