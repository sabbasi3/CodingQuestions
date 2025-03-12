# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root,min_val,max_val):
            if not root:
                return True  
            if not (min_val < root.val < max_val):
                return False

            isLeft = dfs(root.left, min_val, root.val)
            isRight = dfs(root.right, root.val, max_val)

            return isLeft and isRight

        
        return dfs(root, float('-inf'),float('inf'))