# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def helper(root,path):
            path+="->"+str(root.val)
            if not root.left and not root.right:
                res.append(path[2:])
                return 
            if root.left:
                helper(root.left, path)
            if root.right:
                helper(root.right, path)
        
        helper(root,"")
        return res