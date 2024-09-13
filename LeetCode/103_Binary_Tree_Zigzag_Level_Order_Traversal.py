# Definition for a binary tree node.

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return f"{self.val}, {self.left}, {self.right}"
        
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        level = 0
        ans = []
        queue = deque()
        queue.append(root)

        #print(queue)

        while queue:
            curr_len = len(queue)
            curr_queue = list()

            for i in range(curr_len):
                curr = queue.popleft()

                curr_queue.append(curr.val)
            
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if level % 2:
                ans.append(curr_queue[::-1])
            else:
                ans.append(curr_queue)
            level += 1
            
        return ans


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
s = Solution()
print(s.zigzagLevelOrder(root))
        