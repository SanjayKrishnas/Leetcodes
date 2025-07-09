class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #we know that either the max or the min must occur without going around the circular part of the array
        #so by keeping track if both we can discern our final answer
        #we use kadanes algorithm for this 

        absMax, relMax = -float('inf'), 0
        absMin, relMin = float('inf'), 0
        total = 0

        for num in nums:
            total += num
        
        for num in nums:
            relMax = max(relMax + num, num) 
            relMin = min(relMin + num, num)

            absMax = max(absMax, relMax)
            absMin = min(absMin, relMin)

            #print(relMax, absMax)
            #print(relMin, absMin)

        if absMax < 0: return absMax #this means absMax is negative 
        return max(absMax, total - absMin)
