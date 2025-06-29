# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c = [0]
        node = []
        def dfs(root):
            if root and not node:
                dfs(root.left)
                c[0] += 1
                if c[0] == k:
                    node.append(root.val)
                    return 
                dfs(root.right)
        dfs(root)
        return node[0]