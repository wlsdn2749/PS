from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, minimum, maximum):
            if not node:
                return True
            
            if not (node.val > minimum and node.val < maximum):
                return False
            
            return valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)
        
        return valid(root, float('-inf'), float('inf'))
            
s = Solution()
root = TreeNode(2, TreeNode(1), TreeNode(3))
root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
root = TreeNode(0, TreeNode(-1))
root = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
print(s.isValidBST(root))