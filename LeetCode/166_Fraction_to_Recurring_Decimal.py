from collections import deque

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        if numerator == 0: return "0"
        
        neg_sign = "" if ((numerator < 0) == (denominator < 0)) else "-"
        numerator, denominator = abs(numerator), abs(denominator)
        
        quotient = str(numerator // denominator)
        remainder_index, start_index, last_index, decimals, repeating =\
            {}, 0, 0, [], False
            
        if numerator % denominator == 0:
            return neg_sign + quotient
        
        while True:
            
            decimals.append(numerator // denominator)
            remainder = numerator % denominator
            numerator = remainder * 10
            
            if remainder == 0:
                repeating = False
                break
            
            if remainder in remainder_index:
                repeating = True
                start_index = remainder_index[remainder]
                break
            
            remainder_index[remainder] = last_index
            last_index += 1
            
        decimals = ''.join(list(map(str, decimals[1:])))
        
        if not repeating:
            return neg_sign + quotient + '.' + decimals
        
        non_repeating_part = decimals[:start_index]
        repeating_part = decimals[start_index:last_index]
        return neg_sign + quotient + '.' + non_repeating_part + f"({repeating_part})"
            
            
            
            
                
            
                
                
            
        
        
s = Solution()
# print(s.fractionToDecimal(numerator=4, denominator=333)) 
print(s.fractionToDecimal(numerator=3, denominator=14))        