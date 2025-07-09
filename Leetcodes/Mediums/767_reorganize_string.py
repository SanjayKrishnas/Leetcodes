import heapq
from collections import defaultdict

class Solution:
    def reorganizeString(self, s: str) -> str:
        #O(nlogn)
        #we use a heap to get the max occuring character each time
        #then we take the max char and put it into the result string
        #if it is the same as the previous char then we don't use it
        #so we just pop it and then pop athe next element and put it into the result

        charmap = defaultdict(int)
        
        for char in s:
            charmap[char] += 1
        
        charheap = []

        for key, val in charmap.items():
            heapq.heappush(charheap, (-val, key))


        result = ""
        previous = None

        while charheap:
            print(charheap)
            topval, topkey = heapq.heappop(charheap)

            if topkey == previous: #this means we need to pop again if we can
                if charheap: #if we still have elements to pop
                    nextval, nextkey = heapq.heappop(charheap)

                    #add to the result
                    result += nextkey
                    previous = nextkey

                    #add element back to the heap
                    nextval += 1 
                    if nextval < 0: #LESS THAN 0 since we are working with negative numbers
                        heapq.heappush(charheap, (nextval, nextkey))
                else: #no more elements to pop so this is false
                    break
            else: #this means new element is not the same as previous so we just add it directly
                result += topkey
                previous = topkey

                topval += 1
            
            #!!! In both cases we always add in the top element back in if it is still valid
            if topval < 0: 
                heapq.heappush(charheap, (topval, topkey))

        if len(result) == len(s):
            return result
        else:
            return ""
