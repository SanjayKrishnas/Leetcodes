class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #use a hashmap
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        
        result = []
        def findPermutations(permutation):
            if len(permutation) == len(nums):
                result.append(permutation.copy())
                return

            #use a backtracking solution
            for key, val in hashmap.items():
                if val == 0: continue
                
                permutation.append(key) #add the element
                hashmap[key] -= 1
                findPermutations(permutation) #recurse

                permutation.pop() #remove the element
                hashmap[key] += 1

        findPermutations([])
        return result