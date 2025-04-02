from collections import defaultdict
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #so basically each time one of the cars catches up to  (from behind to front) then we have a fleet
        result = 0

        position_index = [(pos, i) for i, pos in enumerate(position)]
        position_index.sort(reverse=True)

        prev = 0
        for i in range(len(position_index)):
            pos = position_index[i][0]
            spd = speed[position_index[i][1]]

            time = (target - pos) / spd

            #if the car directly behind the prev car can't catch up then NO car can catch up guaranteed since the speeds can only get lower
            if time > prev: #if the car can't catch up then a fleet has been formed
                result += 1
                prev = time

        return result