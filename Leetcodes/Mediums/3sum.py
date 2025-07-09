class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sort the array
        result = [ ]
        
        for i in range(len(nums) - 2):  # Change this to len(nums) - 2
            start = i
            middle = i + 1
            end = len(nums) - 1
            #if start is ever > 0 then you are now done
            if(nums[start] > 0): break

            #dont want to start with the same value twice
            if(start > 0 and nums[start] == nums[start - 1]):
                continue

            while(middle < end):
                value = nums[start] + nums[middle] + nums[end]
                if(value < 0):
                    middle += 1
                elif(value > 0):
                    end -= 1
                elif(value == 0):
                    result.append([nums[start], nums[middle], nums[end]])
                    
                    middle += 1
                    end -= 1

                    while(nums[middle] == nums[middle - 1] and middle < end):
                        middle += 1

        return result