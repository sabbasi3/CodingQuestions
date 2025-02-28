class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: # type: ignore
        ### O(1) space and O(n) time complexity 
        l, r = 0, len(numbers) -1

        while l < r: 
            sum = numbers[l] + numbers[r]
            if sum > target:
                r-= 1
            elif sum < target: 
                l += 1
            else: 
                return [l+1, r+1]

        #### bottom solution works but violates the constant extra space requirement. uses O(n) extra space  ###
        # hashdict = {}

        # for i,num in enumerate(numbers):
        #     if target - num in hashdict:
        #         return [ hashdict[target-num] +1, i+1]

        #     hashdict[num] = i
        