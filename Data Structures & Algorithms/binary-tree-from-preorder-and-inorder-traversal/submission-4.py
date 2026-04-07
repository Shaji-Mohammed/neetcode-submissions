# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        p_index = 0
        i_index = {}
        res = []

        for index, value in enumerate(inorder):
            i_index[value] = index

        def buildSubTree(left, right, preorder, inorder):
            nonlocal p_index, i_index
            if left > right:
                return None
            
            value = preorder[p_index]
            in_order_index = i_index[value]
            p_index += 1

            root = TreeNode(value)

            root.left = buildSubTree(left, in_order_index - 1, preorder, inorder)
            root.right = buildSubTree(in_order_index + 1, right, preorder, inorder)

            return root
        
        return buildSubTree(0, len(i_index) - 1, preorder, inorder)
