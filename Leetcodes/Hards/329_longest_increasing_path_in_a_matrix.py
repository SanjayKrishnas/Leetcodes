class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #DFS + DP
        #we keep a n * m array where dp[i][j] is the longest increasing path starting at position [i][j]
        #We at most calculate dp[i][j] once O(m * n) and to get the value to put inside is basically a dfs or bfs so O(n)
        #so total is O(n^2)

        dp = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]

        def inBounds(i, j):
            if i >= 0 and j >= 0:
                if i < len(matrix) and j < len(matrix[0]):
                    return True
            
            return False

        def findMax(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            
            result = 1 #since path is always inclusive
            for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if inBounds(i + r, j + c) and matrix[i + r][j + c] > matrix[i][j]:
                    curPath = findMax(i + r, j + c)
                    result = max(result, 1 + curPath) #either choose current route or the new route
            
            dp[i][j] = result
            return result

        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                relMax = findMax(i, j)
                result = max(result, relMax)

        return result