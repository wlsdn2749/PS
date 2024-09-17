from typing import List
import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
    
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        # print(left ,right)
        if left < len(nums) and nums[left] == target:
            return [left, right-1]
        else:
            return [-1, -1]
        
    
        
        
s = Solution()
nums = [5,7,7,8,8,10]
nums = [2,2]
nums = [1]
print(s.searchRange(nums=nums, target=1))
        