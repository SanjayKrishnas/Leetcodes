from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #we can keep a hashmap of val -> subarray count
        #instead of keeping track of the subarrays after a certain point
        #instead keep a prefix count starting at posiiton 0

        prefix = defaultdict(int)
        prefix[0] = 1 #0 should always be one no matter what
        result = 0
        total = 0

        for num in nums: #NOTE: instead of k - num, we do total - k!!  this is the insight we have
            total += num
            if total - k in prefix: #this means we can cut out a prefix to get k and add to result 
                result += prefix[total - k]
            
            prefix[total] += 1
        
        return result