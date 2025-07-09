class Solution:
    def jump(self, nums: List[int]) -> int:
        start, end = 0, 0

        result = 0
        while end < len(nums) - 1:
            newEnd = end
            while start <= end:
                newEnd = max(newEnd, start + nums[start])
                start += 1

            end = newEnd
            result += 1 #if end is still less than len(nums) then we need to take another jump
        
        return result