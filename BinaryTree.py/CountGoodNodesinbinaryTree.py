# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0

        def dfs(root,new_max):

            if not root:
                return

            if root.val >= new_max:
                self.count += 1

            new_max = max(new_max, root.val)

            dfs(root.left,new_max)
            dfs(root.right,new_max)

            return self.count 

        if root:
            dfs(root,root.val)

        return self.count