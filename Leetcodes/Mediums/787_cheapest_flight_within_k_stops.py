class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        mindist = [float('inf')] * n
        copy_mindist = [float('inf')] * n

        mindist[src] = 0

        curk = 0
        while curk <= k:
            #copy_mindist = mindist.copy()

            for x, y, p in flights:
                
                if mindist[x] == float('inf'): continue

                copy_mindist[y] = min(copy_mindist[y], mindist[x] + p)
            
            mindist = copy_mindist.copy()
            print(mindist)

            curk += 1
        
        if mindist[dst] != float('inf'):
            return mindist[dst]
        
        return -1
                