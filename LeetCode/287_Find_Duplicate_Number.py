from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        
        while slow != fast:
            print(f"slow = {slow}, fast= {fast}")
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        
        print(f"Cycle Detect slow={slow} fast={fast}")    
        slow = nums[0]
        
        
        while slow != fast:
            print(f"slow = {slow}, fast= {fast}")
            slow = nums[slow]
            fast = nums[fast]

        return slow
    
s = Solution()
print(s.findDuplicate(nums=[2,3,1,4,2]))
# print( s.findDuplicate(nums=[1,3,2,4,2]))
# print(s.findDuplicate(nums=[4,3,1,2,1]))
        
        