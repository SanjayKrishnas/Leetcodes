from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.region = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                #region[i][j] = matrix[i][j] + region[i][j-1] + region[i-1][j] - region[i-1][j-1]
                #replace the line above using getSum function to handle out of bounds checking
                self.region[i][j] = matrix[i][j] + self.getSum(i, j-1) + self.getSum(i-1, j) - self.getSum(i-1, j-1)

    def getSum(self, i, j):
            if i >= 0 and j >= 0:
                return self.region[i][j]
            
            return 0

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #region[row2][col2] - region[row2][col1 - 1] - region[row1-1][col2] + region[row1-1][col1-1]

        result = self.getSum(row2, col2) - self.getSum(row2, col1-1) - self.getSum(row1-1, col2) + self.getSum(row1-1, col1-1)
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)