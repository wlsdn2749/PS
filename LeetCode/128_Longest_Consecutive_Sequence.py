from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)

        def lcs_search(num: int):
            count = 0

            if num in s:
                count += 1
                s.remove(num)
            else:
                return 0

            return count + lcs_search(num-1) + lcs_search(num+1)

    
        result = 0

        for idx, num in enumerate(nums):
            result = max(result, lcs_search(num))

        return result
            
