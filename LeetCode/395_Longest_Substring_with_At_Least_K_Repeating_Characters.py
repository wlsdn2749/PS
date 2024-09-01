from collections import defaultdict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        
        substr_length = 0   
            
            
            
        def check_validation(substr: str):
            nonlocal substr_length
            dd = defaultdict(int)
        
            for c in substr:
                dd[c] += 1
            
            temp = str()    
            for c in substr:
                if dd[c] >= k:
                    temp += c
                
                else:
                    check_validation(temp[:])
                    temp = str()
                    
            if len(temp) < len(substr):         
                check_validation(temp[:])     
            
                    
            elif len(temp) == len(substr):
                substr_length = max(substr_length, len(substr))
                    
        check_validation(s)
        return substr_length
                    
                
            
s = Solution()
print(s.longestSubstring(s="abcabcabdc", k=3))
print(s.longestSubstring(s="aaabb", k=3))
print(s.longestSubstring(s="bbaaacbd", k=3))