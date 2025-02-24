# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0 # Depth of an empty tree is 0

        leftmax = self.maxDepth(root.left)
        rightmax = self.maxDepth(root.right)

        return max(leftmax,rightmax) + 1
    
    ### Alternative solution BFS ####
    # number of levels is the same as the depth 
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        q = deque 
        q.append(root)
        level = 0

        while q:

            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
  

            level += 1
    

        return level
    
    ### Iterative DFS ### 

    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        stack = [[root,1]] 
        res = 0

        while stack:
                
            node, depth = stack.pop()
            if node:
                res = max(res,depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res