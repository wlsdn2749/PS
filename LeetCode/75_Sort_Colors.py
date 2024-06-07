from collections import deque
from typing import List

class Solution(object):
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                
            print(f"low: {low} mid: {mid} high: {high} nums: {nums}")

s = Solution()
s.sortColors(nums=[2,1,0,1,2,1,2,0,0])