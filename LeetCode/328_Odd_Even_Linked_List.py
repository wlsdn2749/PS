# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head 

        odd_fst = ListNode()
        odd = odd_fst 
        
        even_fst = ListNode()
        even = even_fst
        
        idx = 0
        while head:
            if idx % 2 == 0:
                odd.next = head
                odd = odd.next

            else:
                even.next = head
                even = even.next
                
            head = head.next
            idx += 1
            
        even.next = None
        odd.next = even_fst.next
        return odd_fst.next
    

        
        