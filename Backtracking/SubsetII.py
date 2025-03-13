class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        subset = []
        nums.sort()
        
        def dfs(i):

            if i >= len(nums):
                if subset not in res:
                    res.append(subset[:])
                return 
            
            subset.append(nums[i])
            dfs(i+1)
            

            subset.pop()

            #skip duplicate values
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            dfs(i+1)


        dfs(0)
        return res


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        subset=[]
        def backtrack(start):
            res.append(subset[:])
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()
        backtrack(0)        
        return res