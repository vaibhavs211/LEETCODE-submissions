# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = [0]

        def dfs(node):
            if not node:
                return 0
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            d[0] = max(d[0], leftHeight + rightHeight)
            return max(leftHeight, rightHeight) + 1

        dfs(root)
        return d[0]