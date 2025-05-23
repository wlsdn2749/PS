from typing import List
import bisect
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        dp = [[] for _ in range(target+1)]
        candidates.sort()

        for idx, candidate in enumerate(candidates):
            if candidate > target:
                continue
            dp[candidate].append([candidate])

        for i in range(target+1):
            idx = bisect.bisect_left(candidates, i)
            for sub_candidate in candidates[:idx]:
                for lst in dp[i - sub_candidate]:
                    temp = sorted(lst + [sub_candidate])
                    if temp not in dp[i]:
                        dp[i].append(temp)
                    # print(lst)
        [print(dp[i]) for i in range(len(dp))]
        return dp[target]
    
s = Solution()
print(s.combinationSum(candidates=[2,3,6,7], target=7))
            

            