class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total=sum(nums)
        leftsum=0
        for i in range(len(nums)):
            if leftsum==total-leftsum-nums[i]:
                return i
            leftsum+=nums[i]
        return -1



    

    


    
