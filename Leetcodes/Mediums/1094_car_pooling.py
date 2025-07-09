import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        starts = []
        ends = []

        for p, s, e in trips:
            starts.append((s, p))
            ends.append((e, p))

        heapq.heapify(starts)
        heapq.heapify(ends)

        total = 0
        while ends or starts:
            if starts and ends:
                shead = starts[0][0]
                ehead = ends[0][0]

                if shead < ehead:
                    total += starts[0][1]
                    if total > capacity: return False
                    heapq.heappop(starts)
                else:
                    total -= ends[0][1]
                    heapq.heappop(ends)
            elif ends:
                return True
        
        return True

            