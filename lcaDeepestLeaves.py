# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def maxDepth (root):
            
            depth = 0
            if not root:
                return 0
            depth = max(maxDepth(root.left) , maxDepth(root.right))
            return 1 + depth
        
        maximum = maxDepth(root)
        
        def LCA(root , deepest):
            if not root:
                return 0
            if deepest == maximum:
                return root
            
            left = LCA(root.left , deepest + 1)
            right = LCA(root.right , deepest + 1)
            
            if left and right:
                return root
            
            if left:
                return left 
            else:
                return right
        
        return LCA(root , 1)
