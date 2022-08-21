# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def childSum(node):
            if not node:
                return 0
            left = childSum(node.left)
            right = childSum(node.right)
            self.total += abs(left - right)
            return node.val + left + right
        childSum(root)
        return self.total
