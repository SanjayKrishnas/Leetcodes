from types import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        def findSubsets(i, arr):
            if i >= len(nums):
                result.append(arr.copy())
                return

            #do the 2 recursive calls
            #1. we can include the current element in the array and continue
            arr.append(nums[i])
            findSubsets(i + 1, arr)
            arr.pop()

            #2. don't include the current element but the next element cannot be the same as the current one
            num = nums[i]
            while i < len(nums) and nums[i] == num: 
                i += 1

            findSubsets(i, arr)

        findSubsets(0, [])
        return result