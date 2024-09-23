# Definition for a binary tree node.
from typing import Optional, List
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        level_dict = defaultdict(list)
        dq = deque()
        result = []
        
        if root is None:
            return result
        
        dq.append((root, 0))
        
        while dq:
            node, level = dq.popleft()
            level_dict[level].append(node.val)
            
            if node.left:
                dq.append((node.left, level+1))
            if node.right:
                dq.append((node.right, level+1))
        
        for key, value in level_dict.items():
            result.append(value)
        
        return result
        
s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(s.levelOrder(root))
            
            
            
            
        
        
        
        