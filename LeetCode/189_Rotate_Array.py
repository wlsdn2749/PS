from typing import List

class Solution:
    
    
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        
        # Solutions 1, Use Reverse
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        
        # Solution 2. Use Queue, Not In-Place and Slow
        # queue = []
        # k = len(nums) - k
        # while k:
        #     queue.append(nums.pop(0))
        #     k=k-1
            
        # while queue:
        #     nums.append(queue.pop(0))
        
        # Solution 3. Use Indexing and Extends
        # k = len(nums) - k
        # new_lst = nums[0:k]
        
        # del nums[:k]
        # nums.extend(new_lst)
        
        # Solution 4. Index Copy? .. 
        
        # n = len(nums)
        # k %= n
        # nums[:] = nums[n-k:] + nums[:n-k]
        
            
    def reverse(self, nums, start, end):
        while start < end:
            nums[end], nums[start] = nums[start], nums[end]
            end-=1; start+=1
            
    
    
nums = [1,2,3,4,5,6,7]
Solution().rotate(nums, 3)
print(nums)

# 7654321
# 4567123

# k=1이면 6만큼
# k=2이면 5만큼
