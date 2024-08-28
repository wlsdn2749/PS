from typing import List
from collections import deque

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False
        
        a = float('inf')
        b = float('inf')
        
        for num in nums:
            if num <= a:
                a = num
            
            elif num <= b:
                b = num
                
            else:
                return True
            
        return False
        
        
        
        
        
            
        
        
            
            
s = Solution()
print(s.increasingTriplet(nums=[1,2,3,4,5]))
print(s.increasingTriplet(nums=[5,4,3,2,1]))
print(s.increasingTriplet(nums=[2,1,5,0,4,6]))
print(s.increasingTriplet(nums=[20,100,10,12,5,13]))
print(s.increasingTriplet(nums=[1,5,0,4,1,3]))


                
                
            
        