# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode]) -> [int,int]:
            if not root:
                return [0,0]
            # first val for tracking height, second for tracking diameter
            h1,d1 = helper(root.left)
            h2,d2 = helper(root.right)
            return [1+max(h1,h2), max(d1, d2, h1+h2)]
        return helper(root)[1]