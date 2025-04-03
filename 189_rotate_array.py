class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def listReverse(start, end):
            while start < end:
                copy = nums[start]
                nums[start] = nums[end]
                nums[end] = copy

                start += 1
                end -= 1
        
        nums.reverse()
        listReverse(0, k - 1)
        listReverse(k, len(nums) - 1)



        
        