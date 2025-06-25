import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #Greedily choose the largest of the 3 values each time and append it to the result if valid
        #time complexity -- O(a + b + c)
        
        maxheap = [] 
        if a > 0: maxheap.append((-a, 'a'))
        if b > 0: maxheap.append((-b, 'b'))
        if c > 0: maxheap.append((-c, 'c'))            

        heapq.heapify(maxheap)
        print(maxheap)
        result = ""

        while maxheap:
            val, char = heapq.heappop(maxheap)
            val = -val #RENEGATE THE NEGATIVE IN THE MAX HEAP
            print(val, char)

            if len(result) >= 2:
                #check if we have the same char 3 times in a row
                if result[-1] == result[-2] == char:
                    if maxheap:
                        next_val, next_char = heapq.heappop(maxheap)
                        next_val = -next_val
                    else:
                        return result #We can no longer continue
                    
                    result += next_char
                    next_val -= 1

                    if next_val > 0:
                        heapq.heappush(maxheap, (-next_val, next_char))

                else:
                    result += char
                    val -= 1
            else:
                result += char
                val -= 1

            if val > 0:
                heapq.heappush(maxheap, (-val, char))
            
            print(result)
        
        return result