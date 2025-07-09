class Solution:
    def rob(self, nums: List[int]) -> int:
        #we run house robber 1 function on [0:len(nums) - 1] and [1:len(nums)]

        #EDGE CASES
        if len(nums) == 1: return nums[0]
        
        def house_robber1(arr):
            result = [0 for i in range(len(arr) + 2)]

            for i in range(len(arr)):
                index = i + 2
                prev = i + 1
                prevprev = i

                result[index] = max(arr[i] + result[prevprev], result[prev])
            
            print(result)
            return result[-1]
        
        num1 = house_robber1(nums[0:len(nums) - 1])
        num2 = house_robber1(nums[1:len(nums)])

        return max(num1, num2)


