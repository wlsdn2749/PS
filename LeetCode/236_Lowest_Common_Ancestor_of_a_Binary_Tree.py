# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def __eq__(self, other):
        return self.val == other.val

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        p_ancestor = []
        q_ancestor = []
        
        def dfs(trace):
            nonlocal p_ancestor, q_ancestor
            
            if p == trace[-1]:
                p_ancestor = trace[:]
            if q == trace[-1]:
                q_ancestor = trace[:]
            
            if trace[-1].left:
                trace.append(trace[-1].left)
                dfs(trace)
                trace.pop()
            
            if trace[-1].right:
                trace.append(trace[-1].right)
                dfs(trace)
                trace.pop()
            
        trace = []
        trace.append(root)
        dfs(trace)
        trace.pop()
        
        lowest_ancestor = None
        for idx, items in enumerate(zip(q_ancestor, p_ancestor)):
            if q_ancestor[idx].val == p_ancestor[idx].val:
                lowest_ancestor = q_ancestor[idx]
            
        return lowest_ancestor
        
root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)


s = Solution()
print(s.lowestCommonAncestor(root=root, p=root.left, q = root.left.right.right))

        