from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        counting_array = [0 for _ in range(max(nums) + 1)]
        
        for num in nums:
            counting_array[num] += 1
            
        
        # even index
        j = max(nums)
        for idx in range(1, len(nums), 2):
            
            while counting_array[j] == 0:
                j-=1
                
            nums[idx] = j
            counting_array[j] -= 1
        
        # odd index
        
        for idx in range(0, len(nums), 2):
            
            
            while counting_array[j] == 0:
                j-=1
                
            nums[idx] = j
            counting_array[j] -= 1
            


        
        
