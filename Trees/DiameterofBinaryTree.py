# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0 

        def height(node):
            if not root:
                return 0
            
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            self.diameter = max(self.diameter, left_height + right_height)

            return max(left_height, right_height) + 1
        

        height(root)
        return self.diameter