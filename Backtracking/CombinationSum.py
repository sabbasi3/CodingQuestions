class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.target = target
        self.subset = []

        def dfs(i,total):

            if total == self.target:
                res.append(self.subset[:])
                return 
            elif total > self.target or i >= len(candidates):
                return 
            
            self.subset.append(candidates[i])

            # case to add the same num
            dfs(i, total + candidates[i])

            self.subset.pop() # remove last number in subset and then go to next num

            # case to add next num
            dfs(i+1, total)


        dfs(0,0) # start with 0 index and 0 total

        return res