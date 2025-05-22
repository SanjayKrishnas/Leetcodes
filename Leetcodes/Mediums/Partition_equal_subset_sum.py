class Solution:
    def canPartition(self, nums: List[int]) -> bool:
            # Optimize by checking for quick fails first
            total = sum(nums)
            if total % 2 != 0:
                return False
            
            target = total // 2
            
            # Sort in descending order - allows earlier pruning
            nums.sort(reverse=True)
            
            # Pre-check: if largest number exceeds target, we can't partition
            if nums[0] > target:
                return False
            
            cache = {}
            def dfs(i, curSum):
                if curSum == target:
                    return True
                if curSum > target or i >= len(nums):
                    return False
                
                if (i, curSum) in cache:
                    return cache[(i, curSum)]
                
                # Try including current element
                if curSum + nums[i] <= target:  # Pruning: only include if it doesn't exceed target
                    include = dfs(i + 1, curSum + nums[i])
                    if include:  # Early return on success
                        cache[(i, curSum)] = True
                        return True
                
                # Try excluding current element
                exclude = dfs(i + 1, curSum)
                
                cache[(i, curSum)] = exclude
                return cache[(i, curSum)]
            
            return dfs(0, 0)
