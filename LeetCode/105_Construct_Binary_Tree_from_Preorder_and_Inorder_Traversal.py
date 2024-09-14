# Definition for a binary tree node.

from typing import List, Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
def preorder_traversal(root):
    result = []
    
    def preorder(node):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
    
    preorder(root)
    return result

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        # 루트는 preorder의 첫 번째 값
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        
        # inorder에서 루트의 위치를 찾아서 왼쪽 서브트리와 오른쪽 서브트리로 나눈다
        inorder_idx = inorder.index(root_val)
        
        # 왼쪽 서브트리와 오른쪽 서브트리를 재귀적으로 구성
        root.left = self.buildTree(preorder, inorder[:inorder_idx])
        root.right = self.buildTree(preorder, inorder[inorder_idx+1:])
    
        return root
    
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
#         node_visited = defaultdict(bool)
        
#         def make_subtree(root, subtree):
#             if root == None:
#                 return
            
#             for idx, node in enumerate(subtree):
#                 if node == root.val:
#                     left = find_left(subtree[:idx])
#                     right = find_right(subtree[idx+1:])
                            
#                     if left:
#                         root.left = TreeNode(left)
#                         make_subtree(root.left, subtree[:idx])
                    
#                     if right:
#                         root.right = TreeNode(right)
#                         make_subtree(root.right, subtree[idx+1:])
                    
                    
#         def find_left(left_subtree):
            
#             for node in preorder:
#                 if node in left_subtree and not node_visited[node]:
#                     node_visited[node] = True
#                     return node
            
#             return None
                
            
#         def find_right(right_subtree):
            
#             for node in preorder:
#                 if node in right_subtree and not node_visited[node]:
#                     node_visited[node] = True
#                     return node
                
#             return None
            
            
#         root = TreeNode(preorder[0])
#         node_visited[preorder[0]] = True
#         make_subtree(root, inorder)
    
#         return root
        
        
s = Solution()
print(preorder_traversal(s.buildTree([3,9,20,15,7], [9,3,15,20,7])))

        