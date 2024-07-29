from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        '''
            Using DP
        '''
        # dp = [1 for _ in range(len(nums))] 
        
        # for idx in range(len(nums)):
        #     for j in range(idx):
        #         if nums[j] < nums[idx] and dp[j]+1 > dp[idx]:
        #             dp[idx] = dp[j] + 1
                    
        # print(dp)
        # return max(dp)
        
        
        '''
            Using Binary Search O(n * log(n))
            
            + if you want? get subsequences
        '''
        def lower_bound(lis: List, num: int):
            start = 0
            end = len(lis)
            while start <= end:
                mid = (start + end) // 2
                if lis[mid] < num:
                    start = mid+1
                else:
                    end = mid-1
            
            return start
                
                
        lis = []
        trace = [] # LIS의 원소가 어떤것이 되는지 추적
        
        for num in nums:
            if lis:
                if num > lis[-1]:
                    lis.append(num)
                    trace.append((num, len(lis)))
                
                else:
                    idx = lower_bound(lis, num)
                    lis[idx] = num
                    trace.append((num, idx+1))
                # num이 마지막 원소보다 크면 가장 마지막에 넣음
                # num이 마지막 원소보다 작을경우
                # lis에 대해 이분탐색해서 Lower Bound 구한 후 대입
            
            else:
                lis.append(num)
                trace.append((num, len(lis)))
        
        trace_bases = len(lis)
        result = []    
        for lis_order in reversed(trace):
            if lis_order[1] == trace_bases:
                result.append(lis_order[0])
                trace_bases -= 1
        
        print(f"an Example of LIS : {list(reversed(result))}") # LIS가 되는 배열중 하나
            
        
        return len(lis)
        
        
    

s = Solution()
print(s.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
print(s.lengthOfLIS(nums = [0,1,0,3,2,3]))
print(s.lengthOfLIS(nums = [7,7,7,7,7,7,7]))
print(s.lengthOfLIS([4,10,4,3,8,9]))
            
            
        