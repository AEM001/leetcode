from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 输出数组先存放前缀积：res[i] = nums[0] * ... * nums[i-1]
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # 再从右往左乘上后缀积：suffix = nums[i+1] * ... * nums[n-1]
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res