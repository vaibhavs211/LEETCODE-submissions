# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def func(node, path):
            if not node:
                return 
            path.append(node.val)
            sm = 0
            for i in range(len(path)-1,-1,-1):
                sm += path[i]
                if sm == targetSum:
                    count[0]+=1
            
            func(node.left, path)
            func(node.right, path)
            path.pop()
            return 
        count = [0]
        func(root, [])
        return count[0]