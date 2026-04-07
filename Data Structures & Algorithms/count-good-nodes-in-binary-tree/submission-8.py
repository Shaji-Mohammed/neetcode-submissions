# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        biggest = -math.inf
        goods = 0

        def dfs(root, biggest):
            nonlocal goods
            if not root:
                return
            if root.val >= biggest:
                
                goods += 1
                biggest = root.val
            
            if root.left:
                dfs(root.left, biggest)
            if root.right:
                dfs(root.right, biggest)

        dfs(root, biggest) 

        return goods