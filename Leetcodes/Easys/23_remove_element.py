class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #either push the val to the end or the NON val elements to the front
        
        if len(nums) == 0: return 0

        start, end = 0, len(nums) - 1

        while start < end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1

        if nums[start] != val:
            return start + 1
        else:
            return start