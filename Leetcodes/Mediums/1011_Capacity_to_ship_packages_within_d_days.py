from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        def testValid(weight):

            result = 0
            cur_weight = 0

            for num in weights:
                cur_weight += num

                if cur_weight == weight:
                    result += 1
                    cur_weight = 0
                elif cur_weight > weight:
                    result += 1
                    cur_weight = num
            
            if cur_weight > 0:
                result += 1
                
            if result > days: return False
            else: return True

        while left <= right:
            mid = (left + right) // 2
            
            if testValid(mid): #if valid then we go to next min
                right = mid - 1
                result = mid
            else:
                left = mid + 1
        

        return result
        