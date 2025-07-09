class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        cur = []

        def backtrack(i):
            if len(cur) == k:
                result.append(cur.copy())
                return
            if i > n:
                return
            
            for j in range(i, n + 1):
                cur.append(j)

                backtrack(j + 1)

                cur.pop()
            
            return
        
        backtrack(1)

        return result