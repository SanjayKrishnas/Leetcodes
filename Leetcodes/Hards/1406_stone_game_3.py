class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        nums = stoneValue
        cache = {} #cache will store (Alice, i) 2n

        def recur(Alice, i):
            if i >= len(stoneValue): return 0

            if (Alice, i) in cache: return cache[(Alice, i)]

            if Alice: #It is Alice's turn
                A1, A2, A3 = -float('inf'), -float('inf'), -float('inf')

                A1 = nums[i] + recur(False, i + 1)
                if i < len(nums) - 1:
                    A2 = nums[i] + nums[i+1] + recur(False, i + 2)
                if i < len(nums) - 2:
                    A3 = nums[i] + nums[i+1] + nums[i+2] + recur(False, i + 3)

                score = max(A1, A2, A3)
            else: #Bob's turn
                B1 = recur(True, i + 1)
                B2 = recur(True, i + 2)
                B3 = recur(True, i + 3)

                score = min(B1, B2, B3)
            
            cache[(Alice, i)] = score
            return score

        Alice = recur(True, 0)
        Bob = sum(stoneValue) - Alice

        if Alice > Bob: return("Alice")
        elif Bob > Alice: return("Bob")
        else: return("Tie")