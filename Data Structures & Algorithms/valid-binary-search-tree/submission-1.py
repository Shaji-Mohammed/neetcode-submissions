# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = self.check_bounds(root, float('-inf'), float('inf'))
        return res

    def check_bounds(self, root: Optional[TreeNode], lower, upper) -> bool:
        if root is None:
            return True

        if root.val < upper and root.val > lower:
            # left
            left = self.check_bounds(root.left, lower, root.val) 

            # right
            right = self.check_bounds(root.right, root.val, upper)

            return True if left and right else False

        return False
