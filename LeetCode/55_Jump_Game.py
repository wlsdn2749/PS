from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        cur_max = 0
        cur_max_idx = 0
        origin_nums_len = len(nums)
        def backtracking(nums, idx):
            nonlocal cur_max, cur_max_idx, origin_nums_len
            
            
            if nums[0] >= cur_max - cur_max_idx - idx:
                cur_max_idx = idx
                cur_max = nums[0]

            
            print(cur_max, idx)
            if idx == origin_nums_len:
                return False
            
            if cur_max + idx >= origin_nums_len:
                return True
            
            return backtracking(nums[1:], idx+1)
        
        return backtracking(nums, 0)
        
        
            
            
s = Solution()
print(s.canJump(nums=[3,2,1,0,4]))
        
        