class RandomizedSet:

    def __init__(self):
        self.randomized_set = {}
            
    def insert(self, val: int) -> bool:
        if val in self.randomized_set:
            return False
        else:
            self.randomized_set.add(val)
            return True
        

    def remove(self, val: int) -> bool:
        
        if val in self.randomized_set:
            self.randomized_set.remove(val)
            return True
        
        return False 

    def getRandom(self) -> int:
        