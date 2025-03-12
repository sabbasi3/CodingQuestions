class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.target = target
        subset = []

        def dfs(i,total):

            if total == self.target:
                res.append(subset)
                return 
            elif total > self.target or i >= len(nums):
                return 
            
            # case to add the same num
            dfs(i, total + nums[i])

            subset.pop() # remove last number in subset and then go to next num

            # case to add next num
            dfs(i+1, total + nums[i])


        def(0,0) # start with 0 index and 0 total

        return res