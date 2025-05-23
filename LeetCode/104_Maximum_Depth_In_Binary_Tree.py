# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.depth = 0
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
            
        depth = 0

        def get_depth(root: Optional[TreeNode], cnt: int) -> int:
            
            depth = cnt
            
            if root.left:
                depth = max(get_depth(root.left, cnt+1), cnt)
            if root.right:
                depth = max(get_depth(root.right, cnt+1), cnt)    

            self.depth = max(depth, self.depth)
            return depth
        
        get_depth(root=root, cnt=1)

        return self.depth
    
s = Solution()
# print( s.maxDepth(root=TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(2), TreeNode(3)))))
print( s.maxDepth(root=TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))

        
            
        