class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #two heaps
        #initialize minheap with all values initally (-capital)
        capitalheap = []
        #max heap is empty (profit)
        profitheap = []

        #initialize capitalheap
        for i in range(len(capital)):
            heapq.heappush(capitalheap, (capital[i], profits[i]))

        for i in range(k):
            #add all possible values from min heap to max heap as long as head(minheap) <= w
            while capitalheap and capitalheap[0][0] <= w:
                cap, prof = heapq.heappop(capitalheap)

                heapq.heappush(profitheap, -prof) #push the -prof since we need a maxheap

            #pop element from maxheap if possible
            if profitheap:
                prof = -heapq.heappop(profitheap)
                w += prof

        return w
