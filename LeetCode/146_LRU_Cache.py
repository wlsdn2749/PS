from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}        
        self.last_used = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        
        if (item := self.cache.get(key, -1)) >= 0:
            self.last_used.append(key)
            
        return item
    
    def put(self, key: int, value: int) -> None:
          
        if self.cache.get(key):
            self.cache[key] = value       
        elif self.capacity > len(self.cache): 
            self.cache[key] = value
        else:
            while len(self.last_used) != self.capacity:
                self.last_used.popleft()
                
            del self.cache[self.last_used.popleft()] # evicts
            self.cache[key] = value
        
        print(self.cache)
        self.last_used.append(key)    
            


lRUCache = LRUCache(2)
lRUCache.put(1, 1); # cache is {1=1}
lRUCache.put(2, 2); # cache is {1=1, 2=2}
lRUCache.get(1);    # return 1
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    # returns -1 (not found)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    # return -1 (not found)
lRUCache.get(3);    # return 3
lRUCache.get(4);    # return 4