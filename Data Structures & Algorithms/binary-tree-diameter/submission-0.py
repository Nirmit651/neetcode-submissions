# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0
        def diameter(root):
            if root is None:
                return 0
            
            leftDepth = diameter(root.left)
            rightDepth = diameter(root.right)
            
            nonlocal maxDiam
            maxDiam = max(maxDiam, leftDepth + rightDepth)

            return 1 + max(leftDepth, rightDepth)
        
        diameter(root)
        return maxDiam

