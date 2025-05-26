class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #dynamic programming problem
        #we can cache (x, y) where x is the position in string 1 and y is the position in string 2
        if len(s1) + len(s2) != len(s3): return False

        cache = {}
        def interleave(x, y, pos):
            #base case check
            if pos == len(s3): return True

            if (x, y) in cache: return cache[(x, y)]

            dp1 = False
            dp2 = False
            dp3 = False

            #either choose to take from string 1 
            if x < len(s1) and s1[x] == s3[pos]:
                dp1 = interleave(x+1, y, pos+1)
            #choose to take from string 2
            if y < len(s2) and s2[y] == s3[pos]:
                dp2 = interleave(x, y+1, pos+1)
            
            cache[(x, y)] = dp1 or dp2
            return cache[(x, y)]

        return interleave(0, 0, 0)
