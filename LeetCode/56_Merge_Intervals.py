from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []
        
        intervals.sort()
        
        for start, end in intervals:
            if not results:
                results.append([start, end])
                continue
            
            if results[-1][1] >= start: # [[1, 3], [2, 6]] case
                results[-1][1] = max(end, results[-1][1]) # [1, 6] update
            
            elif results[-1][1] < start: # [[2, 6], [8, 10]] case
                results.append([start, end]) # [8, 10] append
                
            
        return results
    
s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
s = Solution()
print(s.merge([[1,4],[2,3]]))
