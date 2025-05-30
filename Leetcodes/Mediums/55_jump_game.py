
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        end = 0
        start = 0

        while start <= end:
            val = nums[start]
            #now we can jump to either end, or the start + val

            end = max(end, start + val)
            if end >= len(nums) - 1: return True #make sure you have >= 

            start += 1

        #if we get to here that means start == end and we can no longer continue
        #so this must mean False
        return False

