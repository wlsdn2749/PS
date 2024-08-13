from collections import deque
import re
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        oper = "+"
        num = 0
        
        st = deque()
        for char in s + "+":
            if char in "+-*/":
                if oper == "+":
                    st.append(num)
                elif oper == "-":
                    st.append(-num)
                elif oper == "*":
                    st[-1] *= num
                elif oper == "/":            
                    st[-1] = int(st[-1] / num)
                
                oper = char
                num = 0
                
            elif char.isdigit():
                num = num * 10 + int(char)
        
        return sum(st)
                

s = Solution()
print(s.calculate(" 3/2 "))
print(s.calculate(" 3+2*2"))
print(s.calculate("3+5/2"))
print(s.calculate("432"))
print(s.calculate("1-1+1"))
print(s.calculate("14-3/2"))
        