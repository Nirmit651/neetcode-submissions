# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root is None:
                return 0

            leftDepth = dfs(root.left)
            if leftDepth == -1:
                return -1

            rightDepth = dfs(root.right)
            if rightDepth == -1:
                return -1

            if abs(leftDepth - rightDepth) > 1:
                return -1

            return 1 + max(leftDepth, rightDepth)

        if dfs(root) == -1:
            return False
        else:
            return True
