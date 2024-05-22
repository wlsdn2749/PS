from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        st = []

        while head:
            st.append(head.val)
            head = head.next

        cnt = 1
        # newNode = ListNode()

        def bt(newNode, cnt):
            
            if cnt == n:
                st.pop()
                return bt(newNode, cnt+1)
            
            if st:
                tempNode = ListNode(st.pop(), newNode)
                return bt(tempNode, cnt+1)

            return newNode
        
        return bt(None, cnt)

s = Solution()
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
head = ListNode(1, None)
head_01 = s.removeNthFromEnd(head, 1)

while head_01:
    print(head_01.val)
    head_01 = head_01.next
        




            
