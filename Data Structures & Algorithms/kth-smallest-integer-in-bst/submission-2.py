# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        curr = root
        res = []

        while stack:
            if curr.left and curr.left.val != -1:
                stack.append(curr.left)
                curr = curr.left
            else:
                curr = stack.pop()
                res.append(curr.val)
                curr.val = -1
                if curr.right:
                    stack.append(curr.right)
                    curr = curr.right
        
        return res[k-1]


