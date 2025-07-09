class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        cache = {} #(Alice, l, r)

        def dp(Alice, l, r):
            if l > r:
                return 0

            if (Alice, l, r) in cache:
                return cache[(Alice, l, r)]
            
            if Alice:
                chooseLeft = piles[l] + dp(False, l+1, r)
                chooseRight = piles[r] + dp(False, l, r-1)
                result = max(chooseLeft, chooseRight)
            else: #Bob's turn
                chooseLeft = dp(True, l+1, r)
                chooseRight = dp(True, l, r-1)
                result = min(chooseLeft, chooseRight)
            
            cache[(Alice, l, r)] = result
            return result
        
        vAlice = dp(True, 0, len(piles) - 1)

        total = 0
        for num in piles: total += num

        vBob = total - vAlice

        if vAlice > vBob: return True
        else: return False