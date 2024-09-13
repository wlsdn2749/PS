
# Definition for a Node.
from typing import Optional
import random

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
    
    def __str__(self):
        return f"[{self.val}, {self.next}, {self.random}]"

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # first solution
        
        if not head:
            return None
        
        old_to_new = {}
        
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val) #copy
            curr = curr.next
            
            
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
            
        return old_to_new[head]
    
    


head = Node(7, Node(13, Node(11, Node(10, Node(1)))))
s = Solution()
print(s.copyRandomList(head))
    

        
        