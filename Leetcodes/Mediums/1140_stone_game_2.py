class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}

        def maxAlice(alice, i, M):
            if i >= len(piles): return 0

            if (alice, i, M) in cache: return cache[(alice, i, M)]

            total = 0
            res = 0 if alice else float('inf')

            for j in range(0, 2*M): #so this is saying we try 1 <= x <= 2M stones
                if i + j >= len(piles): break #can no longer continue since we ran out of piles

                total += piles[j + i]
                if alice: #alice's turn
                    res = max(res, total + maxAlice(False, j + i + 1, max(M, j + 1)))
                else: #bob's turn so we want to minimize the potential to give to alice
                    res = min(res, maxAlice(True, j + i + 1, max(M, j + 1))) #represents how much alice will gain from this point
            
            cache[(alice, i, M)] = res
            return res

        return maxAlice(True, 0, 1)
