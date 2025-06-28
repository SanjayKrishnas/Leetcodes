import math
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for i in range(len(grid[0]) + 1)] for j in range(len(grid) + 1)]
        
        #initialize dp array with float('inf')

        for r in range(len(dp)):
            for c in range(len(dp[0])):
                if r == 0 or c == 0:
                    dp[r][c] = float('inf')

        for r in range(len(grid)):
            for c in range(len(grid[0])):
               
                cur_num = grid[r][c]

                if r == 0 and c == 0:
                    dp[1][1] = cur_num
                    continue

                dp[r+1][c+1] = min(dp[r][c+1], dp[r+1][c]) + cur_num

        for r in dp:
            print(r)
        
        return dp[len(grid)][len(grid[0])]