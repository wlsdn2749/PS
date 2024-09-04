# Definition for a binary tree node.
from typing import Optional
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pq = []
        q = []
        
        q.append(root)
        while q:
            node = q.pop()
            
            if node == None:
                continue
            
            q.append(node.left)
            q.append(node.right)
            
            heapq.heappush(pq, node.val)
            
        for i in range(k):
            result = heapq.heappop(pq)
            # print(result)
            
        return result
        
        
    
s = Solution()
print(s.kthSmallest(root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), k=3))

        