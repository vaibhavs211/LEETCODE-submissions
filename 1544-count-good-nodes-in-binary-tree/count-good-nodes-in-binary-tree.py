# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def func(root,cur_mx):
    if not root:
        return 0
    if root.val >= cur_mx:
        return func(root.left, root.val) + func(root.right, root.val) + 1
    else:
        return func(root.left, cur_mx) + func(root.right, cur_mx)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return func(root, -10000)
            