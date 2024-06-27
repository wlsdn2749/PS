from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if (n := len(nums)) == 1: return 0

        if nums[0] > nums[1]: return 0
        if nums[n-1] > nums[n-2]: return n-1
        
        start = 1
        end = n-2

        while(start <= end):
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            elif nums[mid] < nums[mid-1]:
                end = mid - 1
            
            elif nums[mid] < nums[mid+1]: # 큰쪽으로 이분탐색을 돌림 why? 계속 크게 나오는 경우는 최악의 경우도 답을 구할 수 있지만, 계속 작아지는 경우는 못구함 
                start = mid + 1
        
s = Solution()
print( s.findPeakElement(nums=[1,2,3,1]) ) [1,2,3,4,5,6,7], [1,2,5,4,3,6,7]
