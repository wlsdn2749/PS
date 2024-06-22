from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next
        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case: If the length of the linked list is less than or equal to 1, then the list is already sorted
        if not head or not head.next:
            return head
        
        # Find Mid Point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Mid is slow.next 
        mid = slow.next
        
        # Set slow next to None to separate the left and right halves of linked list
        slow.next = None
        
        # Recursively sort the left and right
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Merge the two sorted halves of the linked list
        dummy = ListNode(0)
        curr = dummy
        
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
                
            curr = curr.next
            
        curr.next = left or right
        return dummy.next
        
            
        