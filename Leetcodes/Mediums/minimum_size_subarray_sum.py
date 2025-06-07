class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 2 pointer sliding window approach
        
        l = 0
        run_sum = 0
        result = float('inf')
        
        r = 0
        while r < len(nums):
            # Add current element to running sum
            run_sum += nums[r]
            
            # Shrink window from left while sum >= target
            while run_sum >= target:
                result = min(result, r - l + 1)
                run_sum -= nums[l]
                l += 1
            
            r += 1
        
        # Return 0 if no valid subarray found, otherwise return result
        return 0 if result == float('inf') else result