from typing import List
from itertools import combinations

class Solution:
    def __init__(self):
        self.palindrome_lst = list()
        
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s[0]]]
        
        for i in range(0, len(s)): # 1~2       
            for slices in combinations(range(1, len(s)), i):

                if self.partition_palindrome(s, slices):
                    self.palindrome_lst.append(self.get_partition_from_idx(s, slices))
        
        return self.palindrome_lst
    def get_partition_from_idx(self, s, slices):
        result = []
        start = 0
        for slice in slices:
            result.append(s[start:slice])
            start = slice
        
        result.append(s[start:])
        return result
        
        
                
    def partition_palindrome(self, s, slices):
        start = 0
        for slice in slices:
            if not self.is_palindrome(s[start:slice]):
                return False
            start = slice
        if self.is_palindrome(s[start:]):
            # print(s[start:-1])
            return True
        return False
         
        
    def is_palindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        if s[0] == s[-1]:
            return self.is_palindrome(s[1:-1])
        
        return False
    
    
s = Solution()
print(s.partition("aab"))
s = Solution()
print(s.partition("a"))
s = Solution()
print(s.partition("bb"))