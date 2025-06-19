from typing import List
from collections import defaultdict
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #Run dijkstras where we want to sort by the minimum height
        #The minimum at each position = max(current position, new position)

        def isValid(r, c):
            if r >= 0 and c >= 0:
                if r < len(heights) and c < len(heights[0]):
                    return True
            
            return False

        minheap = []
        minheap.append((0, 0, 0))

        visited = set()

        while minheap:
            prevHeight, r, c = heapq.heappop(minheap)

            #Visited check
            if (r, c) in visited: continue

            #Answer check
            if r == len(heights) -1 and c == len(heights[0]) - 1:
                #We are in the bottom right
                return prevHeight
            
            #Append all neighbors to the heap
            for nextR, nextC in [[1,0], [-1, 0], [0, 1], [0, -1]]:
                if isValid(r + nextR, c + nextC):
                    curHeight = abs(heights[r + nextR][c + nextC] - heights[r][c])
                    heapq.heappush(minheap, (max(prevHeight, curHeight), r + nextR, c + nextC))
            
            visited.add((r, c))
        
        return -1 #this would be an error