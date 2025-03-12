# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # if not root:
        #     return []

        # q = collections.deque() # type: ignore
        # q.append(root)
        # res = []

        # while q:
        #     level_size = len(q)
        #     current_level = []

        #     for _ in range(level_size):
        #         node = q.popleft()
        #         current_level.append(node.val)

        #         if node.right: # append right node first
        #             q.append(node.right)
        #         if node.left:
        #             q.append(node.left)

        #     if current_level:
        #         res.append(current_level[0])


        # return res 
    
        res = []
        q = collections.deque()
        if root: 
            q.append(root)
            
        while q:
            res.append(q[-1].val)
            
            for i in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
        return res

