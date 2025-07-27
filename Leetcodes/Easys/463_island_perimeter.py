class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        #bfs
        #what we realize is that if we ever hit a border or we hit the ocean then we perimeter += 1

        perimeter = 0
        visited = set()

        def valid(i, j):
            if i >= 0 and i < len(grid):
                if j >= 0 and j < len(grid[0]):
                    return True
            
            return False

        def bfs(i, j):
            nonlocal perimeter

            if (i, j) in visited:
                return

            if grid[i][j] == 0:
                return 
                
            visited.add((i, j))
            #Check all the neighbors 
            for m, n in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if valid(i + m, j + n) and grid[i + m][j + n] == 1:
                    bfs(i + m, j + n)
                else:
                    perimeter += 1

            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                bfs(i, j)

        return perimeter