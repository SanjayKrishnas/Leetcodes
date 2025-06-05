class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = set()
        place = { }

        for n in range(len(nums)):
            if target - nums[n] in numbers:
                return [place[target - nums[n]], n]
            else:
                place[nums[n]] = n
                numbers.add(nums[n])
                
        return []
