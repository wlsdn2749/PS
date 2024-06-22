from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        
        def bt(s):
            while s:
                lastword = s
                for word in wordDict:
                    if s[:len(word)] == word:
                        s = s[len(word):]
                        print(s, lastword)
                        if bt(s):
                            return True
                        s = s + s[len(word):]

                if lastword == s:
                    return False

            return True


        return bt(s)
    

s = Solution()
print( s.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]) )
 
