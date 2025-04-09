from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #O(2n)

        #we go through the string from left to right
        #each letter we get the first occurence and the last occurence
        #then we just count them up from beginning to end
        start_end = {}
        for i in range(len(s)):
            char = s[i]
            if char not in start_end:
                start_end[char] = [i, i]
            else:
                start_end[char][1] = i #change the ending char to the new one
        
        result = []
        i = 0
        while i < len(s):
            start = start_end[s[i]][0]
            end = start_end[s[i]][1]

            while i < end:
                end = max(end, start_end[s[i]][1])
                i += 1
            
            result.append(end - start + 1)
            i += 1


        return result



