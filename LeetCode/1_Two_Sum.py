from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Solution 1 
        # Time Complexity O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # Solution 2
        # Time Complexity O(n)
        num_element_dict = dict()
        for idx, num in enumerate(nums):
            if num_element_dict.get(target - num, -1) >= 0:
                return [idx, num_element_dict[target-num]]
            else:    
                num_element_dict[num] = idx            
                
s = Solution()         
print(s.twoSum(nums=[2,7,11,15], target=9))
            
                    
                    
        