class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        result = 0
        def profits(i, bought):
            nonlocal result

            if i >= len(prices):
                return 0

            #check if we have already solved this subproblem
            if (i, bought) in cache:
                return cache[(i, bought)]

            #3 cases, either we buy, sell, or go on cooldown
            if bought: #if we have bought then we either choose to sell or go cooldown
                sell = profits(i + 2, False) + prices[i]
                cooldown = profits(i + 1, bought)

                cache[(i, bought)] = max(sell, cooldown)
            elif not bought: #we have not bought so choose to buy or go cooldown
                buy = profits(i + 1, True) - prices[i]
                cooldown = profits(i + 1, bought)

                cache[(i, bought)] = max(buy, cooldown)
            
            return cache[(i, bought)]
        
        profits(0, False)
        return cache[(0, False)]