class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #O(n)
        #two pointer
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        seen = set()
        replace, cur = 0, 0

        while cur < len(nums):
            if nums[cur] in seen:
                cur += 1
                continue

            seen.add(nums[cur]) #add to seen set

            if replace == cur:
                cur += 1
                replace += 1
                continue
            else:
                nums[replace] = nums[cur]
                replace += 1
                cur += 1
            
        return replace