# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        mx = [0]
        def helper(root, left, length):
            if not root:
                return 
            if left:
                if root.right:
                    helper(root.right, False, length + 1)
                if root.left:
                    helper(root.left, True, 1)
            else:
                if root.left:
                    helper(root.left, True, length+1)
                if root.right:
                    helper(root.right, False, 1)
            mx[0] = max(mx[0], length)
            
        helper(root, True, 0)
        helper(root, False, 0)
        return mx[0]