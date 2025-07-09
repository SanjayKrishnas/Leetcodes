class MedianFinder:

    def __init__(self):
        #2 HEAPS
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        #1. Add elements to maxheap or minheap depeding on top of maxheap
        if not self.maxheap:
            heapq.heappush(self.maxheap, -num)
        elif num > -self.maxheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)

        #2. Adjust both heaps if they differ by more than 1
        if len(self.maxheap) - len(self.minheap) > 1:
            topnum = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, topnum)
        
        if len(self.minheap) - len(self.maxheap) > 1:
            topnum = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -topnum)

    def findMedian(self) -> float:
        #if maxheap larger than minheap then return maxheap[0]
        #else if minheap larger than maxheap then return minheap[0]
        #else sizes equal then return median of both values
       
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0]) / 2
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()