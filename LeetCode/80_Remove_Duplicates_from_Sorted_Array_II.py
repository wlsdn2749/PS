class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 0
        cur = nums[0]
        count = 0
        target = 0
        if len(nums) <= 2:
            return len(nums)

        for i in range(len(nums)):
            
            if target >= len(nums):
                k = i
                return k

            if count == 2:
                while cur == nums[target]:
                    target+=1
                    if target >= len(nums):
                        k = i
                        return k

            if target >= len(nums):
                k = i
                return k

            if cur == nums[target]: # 중복 수치 최대 2
                nums[i] = nums[target]
                count += 1

            if cur < nums[target]:
                nums[i] = nums[target]
                cur = nums[target]
                count = 1

            target += 1

            k = target
        return k