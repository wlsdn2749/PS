from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n): 
            fast = fast.next

        if not fast: 
            return head.next

        while fast.next: 
            fast, slow = fast.next, slow.next
            
        slow.next = slow.next.next
        return head

s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
# head = ListNode(1, None)
head_01 = s.removeNthFromEnd(head, 2)

while head_01:
    print(head_01.val)
    head_01 = head_01.next
        




            
