class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        opt = [[0 for i in range(n + 1)]
                  for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    opt[i][j] = 1
                else:
                    opt[i][j] = opt[i-1][j] + opt[i][j-1]
        
        return opt[m][n]