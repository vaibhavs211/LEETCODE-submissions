# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = []
        stack = [root1]

        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaves1.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        leaves2 = []
        stack = [root2]
        
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaves2.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return True if leaves1 == leaves2 else False