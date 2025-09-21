class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prior=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                if count>prior:
                    prior=count
                
            else:
                
                count=0
        return prior