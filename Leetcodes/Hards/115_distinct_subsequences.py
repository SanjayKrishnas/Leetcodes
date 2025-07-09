class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        result = [0 for i in range(len(t))]

        for i in range(len(s)):
            char = s[i]
            for j in range(len(t)-1, -1, -1): #traverse it going backwards
                if char == t[j]: #this means we have a match so we need to see if the previous char is there
                    #CASES
                    #j = 0
                    if j == 0:
                        result[j] += 1
                    else: #check if the prev char is not 0 and if not then add it to the current result
                        result[j] += result[j-1]
        
        return result[-1]
