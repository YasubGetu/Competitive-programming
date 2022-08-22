# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0 
        def dfs (root , evenGP , parent):
            if not root:
                return 
            if evenGP:
                self.sum += root.val
            evenGP = (parent%2 == 0)
            dfs(root.left , evenGP , root.val)
            dfs(root.right , evenGP , root.val)
            
        dfs(root , False , 1)
        
        return self.sum
