class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #Greedy
        #first we sort
        #then we take the first and last person and see if they can fit in the same boat
        #1. If they cannot then we send the last person (heavy one) on a boat by themself
        #2. If they both fit then we send the first and last person together and then continue
        #Keep track of total number of boats we used
        
        people.sort()
        
        boats = 0
        l, r = 0, len(people) - 1

        while l <= r:
            left = people[l]
            right = people[r]

            if l == r:
                boats += 1
                l += 1
                r -= 1
            else:
                if left + right <= limit:
                    boats += 1
                    l += 1
                    r -= 1
                else: #dont both fit together so send our the right one on a boat
                    boats += 1
                    r -= 1
                    #left stays the same
        
        return boats

