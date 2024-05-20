class Solution:
    def __init__(self):
        self.telephone_dict = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }

        self.result = set()
    
    def bt(self, li, cur_list) -> list:
        
        if not li:
            self.result = []
            return 
        
        if len(cur_list) == len(li):
            self.result.add(''.join(cur_list))
            return

        for d in li:
            for s in self.telephone_dict[d]:
                cur_list.append(s)
                self.bt(li, cur_list)
                cur_list.pop(-1)

    def letterCombinations(self, digits: str):
        li = [*digits]
        self.bt(li, [])

        return self.result
    
s = Solution()
print( s.letterCombinations("23") )

                

        

        
        
        