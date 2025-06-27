# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        sol = []
        def func(node, sm, path):
            if not node:
                return 
            sm += node.val
            path.append(node.val)
            if not node.left and not node.right:
                if sm == targetSum:
                    sol.append(path[:])
                    path.pop()
                    return 
            func(node.left, sm, path)
            func(node.right, sm, path)
            path.pop()
            return 
        func(root, 0, [])
        return sol
