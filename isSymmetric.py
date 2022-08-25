# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [root.left , root.right]
        while len(queue) > 0:
            left = queue.pop(0)
            right = queue.pop(0)
            if not left and not right:
                continue
            if left and right and left.val == right.val:
                pass
            else:
                return False
            
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
            
        return True    
