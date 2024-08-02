import random

class RandomizedSet:

    def __init__(self):
        self.a, self.d = [], {}

            
    def insert(self, val: int) -> bool:
        if val not in self.randomized_set:
            self.d[val] = len(self.a)
            self.a.append(val)
            
            return True

    def remove(self, val: int) -> bool:
        
        if val in self.d:
            e, i = self.a.pop(), self.d.pop(val)
            if i < len(self.a):
                self.a[i], self.d[e] = e, i

            return True

    def getRandom(self) -> int:
        return self.choice(self.a)
    

randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))
print(randomizedSet.insert(2))
print(randomizedSet.remove(2))
print(randomizedSet.getRandom())
print(randomizedSet.remove(1))
print(randomizedSet.insert(2))
print(randomizedSet.getRandom())