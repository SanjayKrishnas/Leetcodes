class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0: 
            return False

        target = sum(matchsticks) // 4
        
        # Early termination: if any matchstick is longer than target
        if any(stick > target for stick in matchsticks):
            return False
        
        # Sort in descending order for better pruning
        matchsticks.sort(reverse=True) #KEY OPTIMIZATION
        
        sides = [0, 0, 0, 0]

        def backtrack(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == target
            
            for j in range(4):
                # Skip if adding this matchstick exceeds target
                if sides[j] + matchsticks[i] > target:
                    continue
                
                # Key optimization: skip duplicate empty sides
                if j > 0 and sides[j] == sides[j-1]:
                    continue
                
                sides[j] += matchsticks[i]
                if backtrack(i + 1):
                    return True
                sides[j] -= matchsticks[i]
            
            return False

        return backtrack(0)