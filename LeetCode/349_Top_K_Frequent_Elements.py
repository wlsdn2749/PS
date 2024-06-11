from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dd = defaultdict(int)
        
        for i in nums:
            dd[i] += 1
            
            
        # Solution 1, Max Heap
        # max_heap = []
            
        # for key,v in dd.items():
        #     heapq.heappush(max_heap, (-v,key))
            
        # return [heapq.heappop(max_heap)[1] for _ in range(k)]
        
        
        # Solution2, Dictionary Sort
        return [i[0] for i in list(sorted(dd.items(), key=lambda x:-x[1]))[:k]]
        
        # Solution3. bucket Sort
        # bucket = [[] for _ in range(len(nums)+1)]
        
        # for key, v in dd.items():
        #     bucket[v].append(key)
        
        # topK = []
        # count=0
        
        # for keys in bucket[::-1]:
        #     if keys:
        #         for key in keys:
        #             count += 1
        #             topK.append(key)
        #             if count == k:
        #                 return topK
            
            
            
        
s = Solution()
result = s.topKFrequent(nums = [4,1,-1,2,-1,2,3], k = 2)

print(result)

