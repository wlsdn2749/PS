from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prod = 1
        global_max = -1e12
        
        for idx in range(len(nums)):
                            
            prod = prod * nums[idx]
            global_max = max(global_max, prod)
            if nums[idx] == 0:
                prod = 1
        
        prod = 1
        
        for idx in range(len(nums)-1, -1, -1):
                
            prod = prod * nums[idx]
            global_max = max(global_max, prod)

            if nums[idx] == 0:
                prod = 1
                
            
        return global_max
            
        
        
s = Solution()
print(s.maxProduct(nums=[-2,1,3,4]))