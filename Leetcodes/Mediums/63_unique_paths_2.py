class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        #BASE CHECK
        if obstacleGrid[0][0] == 1: return 0
        
        for r in range(m + 1):
            if r == 0: continue
            for c in range(n + 1):
                if c == 0: continue

                if r == 1 and c == 1:         
                    dp[1][1] = 1 #one path at start index
                    continue

                if obstacleGrid[r-1][c-1] == 1: 
                    continue #we have to do -1 since our dp array is offset by 1

                dp[r][c] = dp[r-1][c] + dp[r][c-1] #where dp[r-1][c] is the pos above and dp[r][c-1] is to the left

                #DEBBUG
                # for row in dp:
                #     print(row)
                
                # print()
                #DEBUG

        return dp[m][n]