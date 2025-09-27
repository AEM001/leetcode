from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0  # number of zeros seen so far
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[i - count] = nums[i]

        # Fill the last `count` positions with zeros.
        for i in range(len(nums) - count, len(nums)):
            nums[i] = 0

    #   write = 0
    #     for read in range(len(nums)):
    #         if nums[read] != 0:
    #             nums[write] = nums[read]
    #             write += 1

    #     # Second pass: fill the remaining positions with zeros.
    #     for i in range(write, len(nums)):
    #         nums[i] = 0