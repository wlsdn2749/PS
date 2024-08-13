from collections import deque

class Solution:
    def getSum(self, a: int, b: int) -> int:
        a = self.int_to_2bit(a)
        b = self.int_to_2bit(b)
        result = deque()
        
        while len(a) != len(b):
            if len(a) > len(b):
                b = "0" + b
            else:
                a = "0" + a
        print(a,b)
        ceil = 0
        for idx in range(len(a)-1, -1, -1):
            a_idx, b_idx = int(a[idx]), int(b[idx])
            if self.xor(a_idx, b_idx): # xor == 1
                if ceil == 0:
                    result.append(1)
                    ceil = 0
                elif ceil == 1:
                    result.append(0)
                    ceil = 1
            elif not self.xor(a_idx, b_idx):
                if a_idx | b_idx == 0:
                    if ceil == 0:
                        result.append(0)
                        ceil = 0
                    elif ceil == 1:
                        result.append(1)
                        ceil = 0
                if a_idx | b_idx == 1:
                    if ceil == 0:
                        result.append(0)
                        ceil = 1
                    elif ceil == 1:
                        result.append(1)
                        ceil = 1
        if ceil == 1:
            result.append(1)
            
        final = 0
        count = 0
        print(result)
        while list(reversed(result)):
            final += 2 ** count * result.popleft()
            count += 1
            
        return final
    
    def xor(self, a: int, b: int):
        if a != b:
            return 1
        else:
            return 0
            
            
                
        
        
        
        
    def int_to_2bit(self, integer: int) -> str:
        dq = deque()
        result = ""
        while integer >= 1:
            dq.append(str(integer % 2))
            integer //= 2
        
        while dq:
            result += dq.pop()
            
        return result
            
        
        
        
s = Solution()
print(s.getSum(a=20, b=30))

