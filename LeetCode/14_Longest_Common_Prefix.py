from typing import List 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort(key=len)
        lcp = []
        
        for i in range(len(strs[0])):
            candidate = ''    
            for s in strs:
                if not candidate:
                    candidate = s[i]
                
                if s[i] != candidate:
                    return "".join(lcp)
                
            lcp.append(candidate)
        
        return ''.join(lcp)
    

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"])) 