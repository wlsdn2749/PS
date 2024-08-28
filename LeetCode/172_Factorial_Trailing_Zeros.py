class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        zeros = 0
        
        i = 5
        while i <= n:
            zeros += n // i 
            i *= 5
                
        return zeros
            
            
s = Solution()
print( s.trailingZeroes(n=9401) )