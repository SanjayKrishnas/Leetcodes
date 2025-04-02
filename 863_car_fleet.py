from collections import defaultdict
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #minimum speed of any car in the fleet
        #this means if the cars become a fleet then they go at the speed of the slowest car
        #so at each interval we need to see if two cars are at the same position at any point of time
        result = 0
        complete = 0

        while complete < len(position):
            #update positions
            pos_spd = defaultdict(list)
            for i in range(len(position)):
                pos = position[i]
                spd = speed[i]
                if pos >= target: continue

                #increment all the spots
                position[i] += speed[i]
                pos_spd[position[i]].append(i)

            #check completions
            for key, val in pos_spd.items():
                if key >= target:
                    result += 1
                    complete += len(val)

            #update speeds accordingly
            for key, val in pos_spd.items():
                rel_min = speed[val[0]]

                for i in val: #get min speed
                    rel_min = min(rel_min, speed[i])
                
                for i in val: #reassign the min speed
                    speed[i] = rel_min
            
            #now we want to check if any of them are the same

        print(position)
        print(speed)
        return result
