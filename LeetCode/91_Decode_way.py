

class Solution:
    def __init__(self):
        self.hash = {}
        
    def numDecodings(self, s: str) -> int:
        return self.rec(s)
    
    def rec(self, s: str) -> int:
        if s in self.hash:
            return self.hash[s]
        if s.startswith('0'):
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 1

        res = self.rec(s[1:])

        if int(s[:2]) <= 26:
            res += self.rec(s[2:])

        self.hash[s] = res
        return res