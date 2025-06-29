from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10:0, 20:0}

        for i, num in enumerate(bills):
            change[num] += 1
            
            num = num - 5

            if num == 5: #get 10 dollars
                change[5] -= 1

                if change[5] < 0:
                    return False
            elif num == 15: #get 20 dollars
                if change[10] > 0:
                    change[5] -= 1
                    change[10] -= 1

                    if change[5] < 0 or change[10] < 0:
                        return False
                else:
                    change[5] -= 3
                    if change[5] < 0:
                        return False

        
        return True