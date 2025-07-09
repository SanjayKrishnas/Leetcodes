class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #O(N^2)to create a hashmap of the points to other points
        #but we can actually just do this as we go so should be fine

        minheap = [] #going to store tuples of (dist, x, y) dist and point
        minheap.append((0, points[0][0], points[0][1]))

        result = 0
        visited = set()
        #run prim's algorithm
        while minheap:
            #get top value which is the next possible minimum
            mindist, x, y = heapq.heappop(minheap)
            if (x,y) in visited: continue #point has already been added

            #ELSE CASE
            result += mindist
            visited.add((x,y))

            #now add all the other points to the minheap
            for newx, newy in points:
                if (newx, newy) in visited: continue
                
                newdist = abs(newx - x) + abs(newy - y)
                heapq.heappush(minheap, (newdist, newx, newy))

        return result
