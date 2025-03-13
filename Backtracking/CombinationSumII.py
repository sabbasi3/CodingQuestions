class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        subset = []
        self.target = target
        candidates.sort()
        
        def dfs(i, total):

            if total == self.target:
                res.append(subset[:])
                return
            if i >= len(candidates) or total > self.target:
                return
            
            subset.append(candidates[i])

            # case to add next num
            dfs(i+1,total + candidates[i])

            subset.pop() # case to skip most recent added num


            #skip duplicate values
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i+1,total)


        dfs(0,0)
        return res
