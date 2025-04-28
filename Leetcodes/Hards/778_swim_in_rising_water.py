class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        minHeap = [] #keep a minheap for our grid (minheap so no need to negate the values)
        heapq.heappush(minHeap, (grid[0][0], 0, 0))
        visited = set()
        visited.add((0,0))

        def inBounds(r, c):
            if r < 0 or c < 0: return False
            if r >= len(grid) or c >= len(grid[0]): return False

            return True

        direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while minHeap:
            height, r, c = heapq.heappop(minHeap)
            #if (r,c) in visited: continue #don't revisit the same spot

            if r == len(grid) - 1 and c == len(grid[0]) - 1:#if we reached the bottom then return that value!
                return height
                
            visited.add((r,c))

            #now we add all of the neghbors to the minheap
            for dr, dc in direc:
                newr, newc = r + dr, c + dc
                #if this is inbounds then add it to the heap
                if inBounds(newr, newc) and (newr, newc) not in visited:
                    newLocation = (max(height, grid[newr][newc]), newr, newc)
                    heapq.heappush(minHeap, newLocation)

                    visited.add((newr,newc))

        return height
        #we shouldn't be returning the height in the bottom cell but instead the max height to get to the bottom right cell instead
        #return grid[len(grid) - 1][len(grid[0]) - 1]
