from itertools import product
from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        # ! Memory Exceed
        '''
        left_side = list(map(sum, product(nums1, nums2)))
        right_side = list(map(sum, product(nums3, nums4)))

        return list(map(sum, product(left_side, right_side))).count(0)
        '''
        
        left_two_sum_dict = defaultdict(int)
        right_two_sum_dict = defaultdict(int)
        
        count = 0
        
        for x,y in product(nums1, nums2):
            left_two_sum_dict[x+y] += 1
            
        for x,y in product(nums3, nums4):
            right_two_sum_dict[x+y] += 1

        for k,v in left_two_sum_dict.items():
            count += right_two_sum_dict[-k]*v
            
        return count
        
s = Solution()
print(s.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))
        

            
        