class Solution:
    
    def __init__(self):
        self.rle = ["1", "1"]
        self.func()
        
    def countAndSay(self, n: int) -> str:
        return self.rle[n]
    
    def func(self):
        
        for i in range(30):
            base = self.rle[-1]
            cur = 0
            count = 0
            temp = ""
            while base:
                if cur == 0:
                    cur = base[0]
                    count += 1
                elif cur == base[0]:
                    count += 1
                    
                else:
                    temp += f"{count}{cur}"
                    cur = base[0]
                    count = 1 
                    
                base = base[1:]
            
            temp += f"{count}{cur}"
            self.rle.append(temp)
            
s = Solution()
print( s.countAndSay(4) )